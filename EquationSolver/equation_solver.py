class ExpressionSolver():
    """ Class to solve expressions, 
    
    Usage:
    >>> ExpressionSolver().solve_expression("2x + (3x - 15)^2 - 8")
    9x^2 - 92x + 217
    """
    _groupers = [
        ("(", ")"),
        ("[", "]")
    ]

    def __init__(self, groupers=None):
        self.groupers = groupers or self._groupers

    def solve_expression(self, expression):
        pass
