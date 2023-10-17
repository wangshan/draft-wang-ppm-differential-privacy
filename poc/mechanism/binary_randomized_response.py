"""
Binary randomized response mechanism from Appendix C.1 in
https://arxiv.org/pdf/2211.10082.pdf.
"""

import math

from mechanism import DpMechanism


class BinaryRandomizedResponse(DpMechanism):
    DataType = list[int]
    # Debiasing produces an array of floats.
    DebiasedDataType = list[float]

    def __init__(self, eps0: float):
        self.eps0 = eps0
        self.p = 1.0 / (math.exp(eps0) + 1.0)

    def add_noise(self, data: DataType) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()

    def sample_noise(self, dimension: int) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()

    def debias(self,
               data: DataType,
               meas_count: int) -> DebiasedDataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()


def test():
    rr = BinaryRandomizedResponse(8.0)
    # Expect this to fail before it is implemented.
    rr.sample_noise(100)


if __name__ == '__main__':
    test()
