"""
    This module defines the definition of a measure

    classes:
        Measure
"""

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
