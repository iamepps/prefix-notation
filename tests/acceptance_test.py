import pytest
from src.evaluate import evaluate_expression


test_cases = [(['*', '+', 1, 2, '+', 3, 4], 21),
              (['+', '+', 1, '*', 2, 3, 4], 11),
              (['+', 1, '*', 2, '+', 3, 4], 15),
              (['+', '*', '+', 1, 2, 3, 4], 13)]


def it_calculates():
    for case, result in test_cases:
        print(case, result)
        assert evaluate_expression(case) == result


