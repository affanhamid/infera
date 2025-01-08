"""
    This module defines the sample space class

    classes:
        SampleSpace
"""

from infera.real_analysis.set import Set


class SampleSpace(Set):
    """
    This is the sample space class

    A sample space in measure theory is a universal set that
    contains every possible outcome of an experiment
    """

    def __init__(self):
        super().__init__()
