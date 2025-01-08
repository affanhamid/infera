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

    def __init__(self, domain: Set, codomain: Set, expression: FunctionType):
        self.domain = domain
        self.codomain = codomain
        self.expression = expression

    def __call__(self, *args, **kwargs):
        return self.expression(args, kwargs)


class RealValuedFunction(Function):
    """
    This class defines a function whose codomain is the real field
    """

    def __init__(self, domain: Set, codomain: Set, expression):
        super().__init__(domain, codomain, expression)
