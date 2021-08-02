from typing import Union
from src.config import operators

def remove_whitespace(expression: str) -> str:
    """Remove whitespace from expression"""
    return ' '.join(expression.split())


def string_to_int(string: str) -> Union[int, str]:
    try:
        return int(string)
    except:
        return string


def clean_expression(expression: str) -> list:
    """Clean and split string expression into list of elements
    NB. I forgot if there are rules around valid variable names. Could implement them here"""

    expression = remove_whitespace(expression)

    return [string_to_int(element) for element in expression.split(' ')]


def find_variables(clean_expression: list) -> list:
    """Find variables in an expression"""

    return [element
            for element
            in clean_expression
            if not isinstance(element, int)
            and element not in operators]