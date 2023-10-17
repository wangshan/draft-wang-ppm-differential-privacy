"""
Interface for DP policies.

A DP policy is executed with the corresponding VDAF, and relies on some or
all parties of an aggregation protocol to add the right amount of noise to
ensure the final aggregate result is differentially private. The actual
parties that participate in adding noise depends on the threat model that the
DP policy is designed for.
"""

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
        Add noise to measurement, if required by the Client-DP mechanism.
        The default implementation is to do nothing.
        """
        return meas

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Add noise to aggregate share, if required by the Aggregator-DP mechanism.
        The default implementation is to do nothing.
        """
        return agg_share

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        """
        Debias aggregate result, if any of the Client- or Aggregator-DP
        mechanism requires this operation, based on the number of measurements
        `meas_count`. The default implementation is to do nothing.
        """
        return agg_result
