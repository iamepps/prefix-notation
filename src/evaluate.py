from src.config import operators


def calculate(operator: str, v1: int, v2:int) -> int:
    """Calculate the result of applying an operator to two values
    Arguments:
    operator: mathematical operator
    v1: int
    v2: int
    Returns:
    int:
    None: If operator provided is not one of `+`, `-`, `*`, `/`
    """
    if operator not in operators:
        raise ValueError("Operator not in `+`, `-`, `*`, `/`")

    if operator == "+":
        return v1 + v2

    if operator == "-":
        return v1 - v2

    if operator == "*":
        return v1 * v2

    if operator == "/":
        return v1 // v2


def evaluate_expression(expression: list) -> int:
    try:
        queue = []

        for element in reversed(expression):

            # If element isn't an operator put it aside
            if element not in operators:
                queue.append(element)

            else:
                # Evaluate the two most recent elements in unparsed
                v1 = queue.pop()
                v2 = queue.pop()
                queue.append(calculate(element, v1, v2))

    except Exception as e:
        raise e

    return queue[0]