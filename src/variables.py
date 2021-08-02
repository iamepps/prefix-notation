import re
from itertools import product


def all_combinations_of_variables(variables: dict) -> list:
    """Find all potential combinations of variable values.
    This feels a bit inelegant - I think there is a better way."""

    # zip variable name and potential values from range
    list_of_variable_val_dicts = [[{k: i} for i in range(vals[0], vals[1])] for k, vals in variables.items()]

    # find all combinations of variables / values
    list_of_combinations = product(*list_of_variable_val_dicts)

    # convert tuples to dicts
    tuple_of_dicts_to_dict = lambda x: {k: v for d in x for k, v in d.items()}
    all_combinations = [tuple_of_dicts_to_dict(tup) for tup in list_of_combinations]

    return all_combinations


def generate_candidate_expressions(cleaned_expression: list, variables: dict={}) -> list:
    """Given an expression replace each variable with all potential values to find all possible expresssions"""

    # If no variables are passed, return the expression
    if variables:
        all_variable_combinations = all_combinations_of_variables(variables)
    else:
        return [cleaned_expression]

    output = []

    # Loop through variable combinations and recursively update expression until all variables have been replaced
    for combination in all_variable_combinations:
        updated_expressions = [combination[x] if combination.get(x) else x for x in cleaned_expression]
        output.append(updated_expressions)

    return output
