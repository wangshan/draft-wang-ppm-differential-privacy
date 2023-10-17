"""
A policy that uses only Client-DP to achieve central `(EPSILON, DELTA)`-DP in
the OAMC trust model.

Each Client adds binary randomized response noise with pure `EPSILON_0`-DP. With
the target `batch_size` number of honest Clients, the final aggregate result is
`(EPSILON, DELTA)`-DP. If the number of Clients does not meet `batch_size`, the
batch will be dropped.
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
from flp_generic import MultiHotHistogram

from binary_randomized_response import BinaryRandomizedResponse
from policy import DpPolicy


class MultiHotHistogramWithClientDp(DpPolicy):
    Field = MultiHotHistogram.Field
    Measurement = MultiHotHistogram.Measurement
    AggShare = list[Field]
    AggResult = MultiHotHistogram.AggResult
    DebiasedAggResult = BinaryRandomizedResponse.DebiasedDataType

    def __init__(self, eps0: float):
        # TODO(junyechen1996): Justify how eps0 + min_batch_size can achieve
        # (eps, delta)-DP.
        self.rr = BinaryRandomizedResponse(eps0)

    def add_noise_to_measurement(self,
                                 meas: Measurement,
                                 ) -> Measurement:
        return self.rr.add_noise(meas)

    def debias_agg_result(self,
                          agg_result: AggResult,
                          meas_count: int,
                          ) -> DebiasedAggResult:
        # TODO(junyechen1996): Implement de-biasing.
        raise NotImplementedError()


def test():
    multi_hot_histogram_with_dp = MultiHotHistogramWithClientDp(8.0)
    # Expect this to fail before it is implemented.
    multi_hot_histogram_with_dp.add_noise_to_measurement([0])


if __name__ == '__main__':
    test()
