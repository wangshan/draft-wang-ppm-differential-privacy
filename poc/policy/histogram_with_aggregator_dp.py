"""
A policy that uses only Aggregator-DP to achieve central `(EPSILON, DELTA)`-DP
in the OAOC trust model.

Each Aggregator independently adds discrete Gaussian noise to its aggregate
share, so that as long as at least one Aggregator is honest, the final
aggregate result is `(EPSILON, DELTA)`-differentially private. If both
Aggregators are honest, then we will lose some utility.
"""

import importlib
import math
import os
import sys

# Access files that live in different directories, since currently the source
# files are not module-based.
# `dir_name` points to the `poc` folder in DP draft.
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Access files in `mechanism` folder.
# TODO(junyechen1996): Remove after #24.
sys.path.append(os.path.join(dir_name, "mechanism"))
# Access files in analytic Gaussian mechanism.
sys.path.append(os.path.join(dir_name, "analytic-gaussian-mechanism"))
# Access files in VDAF `poc` folder.
sys.path.append(os.path.join(dir_name, "draft-irtf-cfrg-vdaf", "poc"))
# The file name `agm-example.py` in the git submodule
# `analytic-gaussian-mechanism`is not importable with stand `import`, so use
# `import_module` instead.
agm = importlib.import_module("agm-example")
from flp_generic import Histogram
from vdaf_prio3 import Prio3Histogram

from discrete_gaussian import DiscreteGaussianWithZeroMean
from policy import DpPolicy, run_dp_policy_with_vdaf


class HistogramWithAggregatorDp(DpPolicy):
    Field = Histogram.Field
    # A measurement is an unsigned integer, indicating an index less than
    # `Histogram.length`.
    Measurement = Histogram.Measurement
    AggShare = list[Field]
    AggResult = Histogram.AggResult
    # The final aggregate result should be a vector of signed integers, because
    # discrete Gaussian could produce negative noise that may have a larger
    # absolute value than the count before noise.
    DebiasedAggResult = list[int]

    def __init__(self, epsilon: float, delta: float):
        # TODO(junyechen1996): Consider using fixed precision or large decimal
        # for parameters like `epsilon` and `delta`. (#23)
        # Transforming an one-hot vector into another will affect two
        # coordinates, e.g., transforming an one-hot vector `[1, 0]` to `[0, 1]`
        # changes L2-sensitivity by `sqrt((1 - 0)^2 + (0 - 1)^2) = sqrt(2)`.
        dgauss_sigma = agm.calibrateAnalyticGaussianMechanism(
            epsilon, delta, math.sqrt(2.0)
        )
        self.dgauss_mechanism = \
            DiscreteGaussianWithZeroMean(dgauss_sigma)

    def add_noise_to_agg_share(self,
                               agg_share: AggShare,
                               ) -> AggShare:
        """
        Sample discrete Gaussian noise, and merge it with the aggregate share.
        """
        noise_vec = self.dgauss_mechanism.sample_noise(len(agg_share))
        result = []
        for (agg_share_i, noise_vec_i) in zip(agg_share, noise_vec):
            if noise_vec_i < 0:
                noise_vec_i = Field.MODULUS + noise_vec_i
            result.append(agg_share_i + self.Field(noise_vec_i))
        return result

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        # TODO(junyechen1996): Interpret large unsigned integers as negative
        # values or 0 properly. For now, directly return it, since we haven't
        # fully implemented discrete Gaussian mechanism (#10).
        return agg_result


def test():
    # DP policy with Aggregator-DP only.
    # Expect this to fail before `DiscreteGaussianWithZeroMean` is fully
    # implemented.
    dp_policy = HistogramWithAggregatorDp(0.03, 1e-9)

    dimension = 50
    # Prio3Histogram VDAF with length = dimension, and chunk_length = 10.
    num_shares = 2
    vdaf = Prio3Histogram \
        .with_params(dimension, 10) \
        .with_shares(num_shares)

    # All Clients submit a measurement with the first index.
    batch_size = 10
    measurements = [0] * batch_size
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
