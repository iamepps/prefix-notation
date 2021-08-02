from src.config import operators
from src.clean import find_variables

def expression_is_balanced(expression: list, variables: list=[]) -> bool:
    """Check an expression is valid prefix notation (kind of...).
    .. this doesn't check for valid order e.g. `2 1 +` is invalid but would pass this function
    """

    def count_operands_and_variables(expression, variables=[]):
        """Count operands in the expression"""
        return len([element
                    for element
                    in expression
                    if isinstance(element, int) or element in variables
                    ])

    def count_operators(expression):
        """Count operators in the expression"""
        return len([element for element in expression if element in operators])

    return count_operands_and_variables(expression, variables) - 1 == count_operators(expression)


def expression_is_valid(expression: list) -> bool:
    """Check if expressions meets all criteria"""
    variables = find_variables(expression)
    is_valid = all([expression_is_balanced(expression, variables)])
    return is_valid
