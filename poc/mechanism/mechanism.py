"""
Interface for DP mechanisms.

A DP mechanism is responsible for sampling noise and adding it to the data with
the type applicable to the DP mechanism.
"""

class DpMechanism:
    # The data type applicable to this `DpMechanism`. The type is the same for
    # the noised data and the un-noised data.
    DataType = None
    # Debiased data type after removing bias added by the noise. For most of the
    # mechanisms, `DebiasedDataType == DataType`.
    DebiasedDataType = None

    def add_noise(self, data: DataType) -> DataType:
        """Add noise to a piece of input data. """
        raise NotImplementedError()

    def sample_noise(self, dimension: int) -> DataType:
        """
        Sample noise with the initialized `DpMechanism`. `dimension` is used to
        determine the length of the output if `DataType` is a list.
        """
        raise NotImplementedError()

    def debias(self,
               data: DataType,
               meas_count: int) -> DebiasedDataType:
        """
        Debias the data due to the added noise, based on the number of
        measurements `meas_count`. This doesn't apply to all DP mechanisms.
        Some Client-DP mechanisms need this functionality.
        """
        return data
