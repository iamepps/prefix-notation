#!/bin/python3
from src.clean import clean_expression, find_variables
from src.validate import expression_is_valid
from src.variables import generate_candidate_expressions
from src.evaluate import evaluate_expression

def main():

    expression = input("Please provide a prefix-notation expression: ")

    expression_clean = clean_expression(expression)

    if expression_is_valid(expression_clean):
        variable_names = find_variables(expression_clean)

        variables = {}

        if len(variable_names) > 0:

            for variable in variable_names:
                min_val = int(input(f"Please enter the minimum value of {variable}: "))
                max_val = int(input(f"Please enter the maximum value of {variable}: "))
                variables[variable] = (min_val, max_val)

        candidate_expressions = generate_candidate_expressions(expression_clean, variables)

        results = [evaluate_expression(candidate) for candidate in candidate_expressions]

        print(max(results))

    else:
        print("The expression you entered doesn't appear to be valid. Please try again!")

if __name__ == '__main__':
    main()

