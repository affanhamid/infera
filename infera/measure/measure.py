"""
    This module defines the definition of a measure

    classes:
        Measure
"""

from itertools import combinations
from types import FunctionType

from infera.measure.spaces import MeasurableSpace
from infera.real_analysis.field import Reals
from infera.real_analysis.function import RealValuedFunction


class Measure(RealValuedFunction):
    """
    This is a measure class
    """

    def __init__(self, measurable_space: MeasurableSpace, expression: FunctionType):
        super().__init__(measurable_space.sigma_algebra, Reals(), expression)

    @classmethod
    def validate(cls, measurable_space: MeasurableSpace, measure: "Measure"):
        """
        This function validates a measure with it's measurable space
        """
        if measure.domain != measurable_space.sigma_algebra:
            return False, "Measure's domain is not the sigma algebra"

        if measure.codomain != Reals:
            return False, "Measure's codomain is not reals"

        if measure(frozenset()) != 0:
            return False, "For null set input, measure does not output 0"

        for subset in measurable_space.sigma_algebra:
            if measure(subset) < 0:
                return False, "measure is negative for at least one input"

        for i in range(1, len(measurable_space.sigma_algebra) + 1):
            for comb in combinations(measurable_space.sigma_algebra, i):
                union_result = frozenset.union(*comb)
                sum_result = sum([measure(subset) for subset in comb])
                if union_result != sum_result:
                    return False, "measure does not work for unions"

        return True, ""
