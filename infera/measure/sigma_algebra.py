"""
    This module defines the class definition of a sigma algebra

    classes:
        SigmaAlgebra class
"""

from itertools import combinations

from infera.measure.sample_space import SampleSpace


class SigmaAlgebra(set):
    """
    This class defines the mathematical object sigma algebra.

    Given a set X, a sigma algebra of set X, Y,  is a collection of
    subsets of X with the following properties:

    - Every element of Y must be a subset of X
    - Y must contain the empty set
    - For every set A in Y, the complement of A must be in Y
    - Infinite unions of elements of Y must be in Y

    methods:
    """

    def __init__(self, sample_space: SampleSpace):
        if not bool(sample_space):
            raise ValueError("Underlying set cannot be empty")

        self.underlying_set = sample_space

    @classmethod
    def validate_sigma_algebra(
        cls, sample_space: SampleSpace, sigma_algebra: "SigmaAlgebra"
    ):
        """
        This function tests the given sigma algebra using the axioms:
        1. null set must belong to sigma algebra
        2. sigma algebra is closed under complementation
        3. sigma algebra is closed under countable unions
        """
        # Empty set must belong to sigma algebra
        if frozenset() not in sigma_algebra:
            return False, "empty set not present in sigma algebra"

        # Sigma algebra must be closed under complementation
        for subset in sigma_algebra:
            if frozenset(sample_space) - subset not in sigma_algebra:
                return (
                    False,
                    f"sigma algebra not closed under complementation. Complement of {subset} not found",
                )

        # Sigma algebra must be closed under countable unions

        for i in range(1, len(sigma_algebra) + 1):
            for comb in combinations(sigma_algebra, i):
                union_result = frozenset().union(*comb)
                if union_result not in sigma_algebra:
                    return (
                        False,
                        f"sigma algebra not closed under countable unions. Union of {comb} not present",
                    )

        return True, ""
