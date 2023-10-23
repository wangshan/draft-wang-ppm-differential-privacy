"""
Interface for DP policies.

A DP policy is executed with the corresponding VDAF, and relies on some or
all parties of an aggregation protocol to add the right amount of noise to
ensure the final aggregate result is differentially private. The actual
parties that participate in adding noise depends on the threat model that the
DP policy is designed for.
"""

# Access files that live in different directories, since currently the source
# files are not module-based.
import os
import sys
# `dir_name` points to the `poc` folder in DP draft.
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Access files in VDAF `poc` folder.
sys.path.append(os.path.join(dir_name, "draft-irtf-cfrg-vdaf", "poc"))
from common import gen_rand
from vdaf import Vdaf, pretty_print_vdaf_test_vec, to_le_bytes


class DpPolicy:
    # Client measurement type.
    Measurement = None
    # Aggregate share type, owned by an Aggregator.
    AggShare = None
    # Aggregate result type, unsharded result from all Aggregators.
    AggResult = None
    # Debiased aggregate result type.
    DebiasedAggResult = None

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        """
        Add noise to measurement, if required by the Client randomization
        mechanism. The default implementation is to do nothing.
        """
        return meas

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Add noise to aggregate share, if required by the Aggregator
        randomization mechanism. The default implementation is to do nothing.
        """
        return agg_share

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        """
        Debias aggregate result, if either of the Client or Aggregator
        randomization mechanism requires this operation, based on the number
        of measurements `meas_count`. The default implementation is to do
        nothing.
        """
        return agg_result


# NOTE This is used to generate {{run-dp-policy-with-vdaf}}.
def run_vdaf_with_dp_policy(
    dp_policy: DpPolicy,
    Vdaf: Vdaf,
    agg_param: Vdaf.AggParam,
    measurements: list[DpPolicy.Measurement],
    print_test_vec=False,
    test_vec_instance=0,
):
    """Run the DP policy with VDAF on a list of measurements."""
    nonces = [gen_rand(Vdaf.NONCE_SIZE) for _ in range(len(measurements))]
    verify_key = gen_rand(Vdaf.VERIFY_KEY_SIZE)

    # REMOVE ME
    test_vec = {
        'shares': Vdaf.SHARES,
        'verify_key': verify_key.hex(),
        'agg_param': agg_param,
        'prep': [],
        'agg_shares': [],
        'agg_result': None,  # set below
    }
    type_params = Vdaf.test_vec_set_type_param(test_vec)

    out_shares = []
    for (nonce, measurement) in zip(nonces, measurements):
        assert len(nonce) == Vdaf.NONCE_SIZE

        # REMOVE ME
        prep_test_vec = {
            'measurement': measurement,
            'nonce': nonce.hex(),
            'public_share': None,  # set below
            'input_shares': [],
            'prep_shares': [[] for _ in range(Vdaf.ROUNDS)],
            'prep_messages': [],
            'out_shares': [],
        }

        # Each Client adds Client randomization noise to its
        # measurement.
        noisy_measurement = \
            dp_policy.add_noise_to_measurement(measurement)
        # Each Client shards its measurement into input shares.
        rand = gen_rand(Vdaf.RAND_SIZE)
        (public_share, input_shares) = \
            Vdaf.shard(noisy_measurement, nonce, rand)

        # REMOVE ME
        prep_test_vec['rand'] = rand.hex()
        prep_test_vec['public_share'] = \
            Vdaf.test_vec_encode_public_share(public_share).hex()
        for input_share in input_shares:
            prep_test_vec['input_shares'].append(
                Vdaf.test_vec_encode_input_share(input_share).hex())

        # Each Aggregator initializes its preparation state.
        prep_states = []
        outbound = []
        for j in range(Vdaf.SHARES):
            (state, share) = Vdaf.prep_init(verify_key, j,
                                            agg_param,
                                            nonce,
                                            public_share,
                                            input_shares[j])
            prep_states.append(state)
            outbound.append(share)
        # REMOVE ME
        for prep_share in outbound:
            prep_test_vec['prep_shares'][0].append(
                Vdaf.test_vec_encode_prep_share(prep_share).hex())

        # Aggregators recover their output shares.
        for i in range(Vdaf.ROUNDS-1):
            prep_msg = Vdaf.prep_shares_to_prep(agg_param,
                                                outbound)
            # REMOVE ME
            prep_test_vec['prep_messages'].append(
                Vdaf.test_vec_encode_prep_msg(prep_msg).hex())

            outbound = []
            for j in range(Vdaf.SHARES):
                out = Vdaf.prep_next(prep_states[j], prep_msg)
                (prep_states[j], out) = out
                outbound.append(out)
            # REMOVE ME
            for prep_share in outbound:
                prep_test_vec['prep_shares'][i+1].append(
                    Vdaf.test_vec_encode_prep_share(prep_share).hex())

        # The final outputs of the prepare phase are the output shares.
        prep_msg = Vdaf.prep_shares_to_prep(agg_param,
                                            outbound)
        # REMOVE ME
        prep_test_vec['prep_messages'].append(
            Vdaf.test_vec_encode_prep_msg(prep_msg).hex())
        outbound = []
        for j in range(Vdaf.SHARES):
            out_share = Vdaf.prep_next(prep_states[j], prep_msg)
            outbound.append(out_share)

        # REMOVE ME
        for out_share in outbound:
            prep_test_vec['out_shares'].append([
                to_le_bytes(x.as_unsigned(), x.ENCODED_SIZE).hex()
                for x in out_share
            ])
        test_vec['prep'].append(prep_test_vec)

        out_shares.append(outbound)

    num_measurements = len(measurements)
    # Each Aggregator aggregates its output shares into an
    # aggregate share, and adds any Aggregator randomization
    # mechanism to its aggregate share. In a distributed VDAF
    # computation, the aggregate shares are sent over the network.
    agg_shares = []
    for j in range(Vdaf.SHARES):
        out_shares_j = [out[j] for out in out_shares]
        agg_share_j = Vdaf.aggregate(agg_param, out_shares_j)
        # Each Aggregator independently adds noise to its aggregate
        # share.
        noised_agg_share_j = \
            dp_policy.add_noise_to_agg_share(agg_share_j)
        agg_shares.append(noised_agg_share_j)

        # REMOVE ME
        test_vec['agg_shares'].append(
            Vdaf.test_vec_encode_agg_share(noised_agg_share_j).hex())

    # Collector unshards the aggregate.
    agg_result = Vdaf.unshard(agg_param, agg_shares,
                              num_measurements)
    # Debias aggregate result.
    debiased_agg_result = dp_policy.debias_agg_result(
        agg_result, num_measurements
    )
    # REMOVE ME
    test_vec['agg_result'] = debiased_agg_result
    if print_test_vec:
        pretty_print_vdaf_test_vec(Vdaf, test_vec, type_params)

        os.system('mkdir -p test_vec/{:02}'.format(VERSION))
        with open('test_vec/{:02}/{}_{}.json'.format(
                VERSION, Vdaf.test_vec_name, test_vec_instance), 'w') as f:
            json.dump(test_vec, f, indent=4, sort_keys=True)
            f.write('\n')

    return debiased_agg_result
