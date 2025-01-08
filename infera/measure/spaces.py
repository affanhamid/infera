"""
    This module defines the spaces defined in measure theory:

    classes:
        MeasurableSpace
        MeasureSpace

    2. Measure space: A sample space, it's sigma algebra, and a measure defined
        is a measure space
"""

from infera.measure.sample_space import SampleSpace
from infera.measure.sigma_algebra import SigmaAlgebra


class MeasurableSpace:
    """
    This class defines a measurable space:
    A sample space and it's sigma algebra is together a measurable space
    """

    def __init__(self, sample_space: SampleSpace, sigma_algebra: SigmaAlgebra):
        valid, error_message = SigmaAlgebra.validate_sigma_algebra(
            sample_space, sigma_algebra
        )
        if not valid:
            raise ValueError(f"Sigma algebra invalid, {error_message}")

        self.sample_space = sample_space
        self.sigma_algebra = sigma_algebra
