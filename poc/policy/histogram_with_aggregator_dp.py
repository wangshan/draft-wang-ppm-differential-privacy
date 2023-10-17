"""
A policy that uses only Aggregator-DP to achieve central `(EPSILON, DELTA)`-DP
in the OAOC trust model.

Each Aggregator independently adds discrete Gaussian noise to its aggregate
share, so that as long as at least one Aggregator is honest, the final
aggregate result is `(EPSILON, DELTA)`-differentially private. If both
Aggregators are honest, then we will lose some utility.
"""

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
from flp_generic import Histogram

from discrete_gaussian import DiscreteGaussianWithZeroMean
from policy import DpPolicy


class HistogramWithAggregatorDp(DpPolicy):
    Field = Histogram.Field
    # A measurement is an unsigned integer, indicating an index
    # less than `Histogram.length`.
    Measurement = Histogram.Measurement
    AggShare = list[Field]
    AggResult = Histogram.AggResult
    # The final aggregate result should be a vector of *signed* integers,
    # because discrete Gaussian could produce negative noise which may have
    # a larger absolute value than the count before noise.
    DebiasedAggResult = list[int]

    def __init__(self, epsilon: float, delta: float):
        # TODO(junyechen1996): Compute discrete Gaussian parameter to
        # achieve (eps, delta)-DP based on
        # https://github.com/BorjaBalle/analytic-gaussian-mechanism.
        self.dgauss_mechanism = DiscreteGaussianWithZeroMean(100.0)

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Sample discrete Gaussian noise, and merge it with
        aggregate share.
        """
        raise NotImplementedError()

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        # TODO(junyechen1996): Interpret large unsigned integers as negative
        # values or 0 properly.
        raise NotImplementedError()


def test():
    histogram_with_dp = HistogramWithAggregatorDp(0.03, 1e-9)
    # This should return measurement as-is.
    histogram_with_dp.add_noise_to_measurement(0)
    # Expect this to fail before it is implemented.
    histogram_with_dp.add_noise_to_agg_share(
        [HistogramWithAggregatorDp.Field(0)]
    )


if __name__ == '__main__':
    test()
