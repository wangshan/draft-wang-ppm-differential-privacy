"""
Discrete Laplace sampler from Algorithm 2 of
https://arxiv.org/pdf/2004.00010.pdf.
"""

from mechanism import DpMechanism


class DiscreteLaplaceWithZeroMean(DpMechanism):
    DataType = list[int]
    DebiasedDataType = DataType

    def __init__(self, t: int, s: int):
        # t/s defines the scale of Laplace.
        self.t = t
        self.s = s

    def add_noise(self, data: DataType) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()

    def sample_noise(self, dimension: int) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()


def test():
    laplace = DiscreteLaplaceWithZeroMean(3, 1)
    # Expect this to fail before it is implemented.
    laplace.sample_noise(100)


if __name__ == '__main__':
    test()
