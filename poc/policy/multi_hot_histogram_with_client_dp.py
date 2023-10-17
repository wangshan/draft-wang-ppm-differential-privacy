"""
A policy that uses only Client-DP to achieve central `(EPSILON, DELTA)`-DP in
the OAMC trust model.

Each Client adds binary randomized response noise with pure `EPSILON_0`-DP. With
the target `batch_size` number of honest Clients, the final aggregate result is
`(EPSILON, DELTA)`-DP. If the number of Clients does not meet `batch_size`, the
batch will be dropped.
"""

from scipy.stats import binom

# Access files that live in different directories, since currently the source
# files are not module-based.
import os
import sys
# `dir_name` points to the `poc` folder in DP draft.
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Access files in `mechanism` folder.
# TODO(junyechen1996): Remove after #24.
sys.path.append(os.path.join(dir_name, "mechanism"))
# Access files in VDAF `poc` folder.
sys.path.append(os.path.join(dir_name, "draft-irtf-cfrg-vdaf", "poc"))
from flp_generic import MultiHotHistogram
from vdaf_prio3 import Prio3MultiHotHistogram

from binary_randomized_response import BinaryRandomizedResponse
from policy import DpPolicy, run_dp_policy_with_vdaf


class MultiHotHistogramWithClientDp(DpPolicy):
    Field = MultiHotHistogram.Field
    Measurement = MultiHotHistogram.Measurement
    AggShare = list[Field]
    AggResult = MultiHotHistogram.AggResult
    DebiasedAggResult = BinaryRandomizedResponse.DebiasedDataType

    def __init__(self, eps0: float):
        # TODO(junyechen1996): Justify how eps0 + batch_size can achieve
        # `(EPSILON, DELTA)`-DP.
        self.rr = BinaryRandomizedResponse(eps0)

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        return self.rr.add_noise(meas)

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        return self.rr.debias(agg_result, meas_count)


def compute_max_count_for_multi_hot_histogram(
    rr: BinaryRandomizedResponse,
    dimension: int,
    false_positive_rate: float,
):
    # As specified in {{client-dp-vdaf-robustness}}, we will compute the
    # maximum count of 1s in the noisy Client measurement, `max_count`,
    # such that, for the binomial random variable `C` with number of trials as
    # `dimension - 1`, and probability as `rr.p`, the cumulative distribution
    # function (CDF) satisfies:
    # `Pr(C <= max_count - 1) >= 1 - false_positive_rate`.
    #
    # We will use the inverse survival function with a survival probability
    # of `false_positive_rate`, for the binomial random variable `C`.
    return round(binom.isf(false_positive_rate, dimension - 1, rr.p)) + 1


def test():
    # DP policy with Client-DP only.
    # Note the parameters are only used for testing, and doesn't provide any
    # meaningful DP guarantee.
    dp_policy = MultiHotHistogramWithClientDp(8.0)
    dimension = 50
    batch_size = 20

    # Set false positive rate to be one Client out of 10 batches of
    # `min_batch_size` number of Clients.
    false_positive_rate = 1.0 / (10 * batch_size)
    max_count = compute_max_count_for_multi_hot_histogram(
        dp_policy.rr, dimension, false_positive_rate
    )
    # Prio3MultiHotHistogram VDAF with length = dimension,
    # max_count = max_count, and chunk_length = 10.
    num_shares = 2
    vdaf = Prio3MultiHotHistogram \
        .with_params(dimension, max_count, 10) \
        .with_shares(num_shares)

    # All Clients submit a measurement with the first index set to 1.
    measurements = [ [1] + [0] * (dimension - 1) for _ in range(batch_size)]
    agg_result = run_dp_policy_with_vdaf(
        dp_policy,
        vdaf,
        None,
        measurements,
    )

    # Sanity check the first index should have the dominant count, because
    # even with DP noise, we should still be able to discover the first index
    # has the heavist count since all Clients submit the first index.
    # TODO(junyechen1996): Add proper testing for noise threshold.
    for i in range(1, dimension):
        assert(agg_result[i] < agg_result[0])


if __name__ == '__main__':
    test()
