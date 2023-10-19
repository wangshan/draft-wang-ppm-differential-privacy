"""
Symmetric RAPPOR that was first proposed in https://arxiv.org/abs/1407.6981.
We implement the version from Appendix C.1 in
https://arxiv.org/pdf/2211.10082.pdf.
"""

import math
import random

from mechanism import DpMechanism


class SymmetricRappor(DpMechanism):
    DataType = list[int]
    # Debiasing produces an array of floats.
    DebiasedDataType = list[float]

    def __init__(self, eps0: float):
        self.eps0 = eps0
        self.p = 1.0 / (math.exp(eps0) + 1.0)

    def add_noise(self, data: DataType) -> DataType:
        # Apply binary randomized response at each coordinate, based on
        # Appendix C.1.1 of {{MJTB+22}}.
        return list(map(
            lambda x: 1 - x if self.coin_flip() else x,
            data
        ))

    def sample_noise(self, dimension: int) -> DataType:
        # Sample binary randomized response at each coordinate on an all zero
        # vector.
        return [int(self.coin_flip()) for coord in range(dimension)]

    def debias(self,
               data: DataType,
               meas_count: int) -> DebiasedDataType:
        # Debias the data based on Appendix C.1.2 of {{MJTB+22}}.
        exp_eps = math.exp(self.eps0)
        return list(map(
            lambda x: (x * (exp_eps + 1) / (exp_eps - 1) -
                       meas_count / (exp_eps - 1)),
            data
        ))

    def coin_flip(self):
        return random.random() < self.p


def test():
    rr = SymmetricRappor(8.0)
    measurement = [0, 1, 0, 1]
    noised_measurement = rr.add_noise(measurement)
    assert(all(val in [0, 1] for val in noised_measurement))

    sampled_noise = rr.sample_noise(100)
    assert(all(val in [0, 1] for val in sampled_noise))

    agg = [2, 1, 0, 1]
    meas_count = 2
    expected_debiased = [2.0006711504016828, 1.0, -0.0006711504016824899, 1.0]
    actual_debiased = rr.debias(agg, meas_count)
    for (actual, expected) in zip(actual_debiased, expected_debiased):
        assert(math.isclose(actual, expected, abs_tol = 1e-6))


if __name__ == '__main__':
    test()
