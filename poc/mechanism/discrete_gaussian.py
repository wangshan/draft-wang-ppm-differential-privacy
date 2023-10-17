"""
Discrete Gaussian sampler from Algorithm 3 of
https://arxiv.org/pdf/2004.00010.pdf.
"""

from mechanism import DpMechanism


class DiscreteGaussianWithZeroMean(DpMechanism):
    DataType = list[int]
    DebiasedDataType = DataType

    def __init__(self, sigma: float):
        # TODO: Consider using fixed precision or rationals to represent this
        # parameter (#23).
        self.sigma = sigma

    def add_noise(self, data: DataType) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()

    def sample_noise(self, dimension: int) -> DataType:
        # TODO: Implement this (#10).
        raise NotImplementedError()


def test():
    dgauss = DiscreteGaussianWithZeroMean(2.0)
    # Expect this to fail before it is implemented.
    dgauss.sample_noise(100)


if __name__ == '__main__':
    test()
