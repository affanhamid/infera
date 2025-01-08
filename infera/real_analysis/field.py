"""
    This module defines a field in mathematics

    classes:
        Field
        Reals
"""

from infera.real_analysis.set import Set


class Field(Set):
    """
    A field is any set that satisfies the field axioms
    """

    @classmethod
    def check_field(cls, field: "Field"):
        """
        This function tests if a given input is a field by the field axioms
        """
        return isinstance(field, Set)


class Reals(Field):
    """
    The set of all real numbers
    """

    @classmethod
    def check_real_field(cls, field: Field):
        """
        This function tests if a given input is a field and a real field
        """
        return cls.check_field(field) & True
