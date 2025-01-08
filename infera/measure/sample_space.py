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

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)

    @classmethod
    def validate(cls, sample_space: Set):
        """
        Function to validate if a given set is a sample space
        Checks for:
        - Whether the sample space is empty
        """
        return bool(sample_space), ""
