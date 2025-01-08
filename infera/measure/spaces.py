"""
    This module defines the spaces defined in measure theory:

    classes:
        MeasurableSpace
        MeasureSpace
"""

from infera.measure.measre import Measure
from infera.measure.sample_space import SampleSpace
from infera.measure.sigma_algebra import SigmaAlgebra


class MeasurableSpace:
    """
    This class defines a measurable space:
    A sample space and it's sigma algebra is together a measurable space
    """

    def __init__(self, sample_space: SampleSpace, sigma_algebra: SigmaAlgebra):

        self.sample_space = sample_space
        self.sigma_algebra = sigma_algebra

    @classmethod
    def validate(cls, measurable_space: "MeasurableSpace"):
        """
        This function validates a measurable space
        """

        valid, error_message = SampleSpace.validate(measurable_space.sample_space)
        if not valid:
            return False, f"Sample space invalid, {error_message}"

        valid, error_message = SigmaAlgebra.validate(
            measurable_space.sample_space, measurable_space.sigma_algebra
        )
        if not valid:
            return False, f"Sigma algebra invalid, {error_message}"

        return True, ""


class MeasureSpace:
    """
    This class defines a Measure space: A sample space, it's sigma algebra, and
    a measure defined on the sigma algebra
    """

    def __init__(self, measurable_space: MeasurableSpace, measure: Measure):
        self.measurable_space = measurable_space
        self.measure = measure

    @classmethod
    def validate(cls, measure_space: "MeasureSpace"):
        valid, error_message = MeasurableSpace.validate(measure_space.measurable_space)
        if not valid:
            return False, f"Measure space invalid, {error_message}"

        valid, error_message = Measure.validate(measure_space.measure)
        if not valid:
            return False, f"Measure space invalid, {error_message}"

        return True, ""
