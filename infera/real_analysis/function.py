"""
    This module defines a function in mathematics

    classes:
        RealValuedFunction
"""

from types import FunctionType

from infera.real_analysis.set import Set


class Function:
    """
    This class defines a generic mathematical function
    """

    def __init__(self, domain: Set, codomain: Set):
        self.domain = domain
        self.codomain = codomain


class RealValuedFunction(Function):
    """
    This class defines a function whose codomain is the real field
    """

    def __init__(self, domain: Set, codomain: Set, expression: FunctionType):
        super().__init__(domain, codomain)
        self.expression = expression
