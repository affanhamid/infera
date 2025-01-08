"""
    This module defines the probability class

    classes:
        Probability
"""

from infera.measure.measure import Measure
from infera.measure.spaces import MeasurableSpace


class ProbabilityMeasure(Measure):
    @classmethod
    def validate(
        cls,
        measurable_space: MeasurableSpace,
        probability_measure: "Measure",
    ):
        super().validate(measurable_space, probability_measure)
        if probability_measure(measurable_space.sample_space) != 1:
            return False, "P(Sample space) is not 1"

        return True, ""
