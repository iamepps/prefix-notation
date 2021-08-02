import pytest
from src.evaluate import calculate, evaluate_expression
from src.variables import all_combinations_of_variables, generate_candidate_expressions
from src.clean import remove_whitespace, string_to_int, clean_expression
from src.validate import expression_is_balanced, expression_is_valid


def it_evaluates_all_operators():
    assert calculate("+", 1, 2) == 3
    assert calculate("*", 1, 2) == 2
    assert calculate("-", 1, 2) == -1
    assert calculate("/", 4, 2) == 2
    assert calculate("/", 5, 2) == 2
    with pytest.raises(ValueError):
        calculate("&", 1, 3)


def it_finds_all_combinations():
    assert all_combinations_of_variables({"a": (1, 2), "b": (3, 5)}) == [{'a': 1, 'b': 3}, {'a': 1, 'b': 4}]
    assert all_combinations_of_variables({"a": (1, 3)}) == [{'a': 1}, {'a': 2}]


def it_finds_all_expressions():
    assert generate_candidate_expressions(['+', 'x', 2], {'x': (1, 3)}) == [['+',  1, 2], ['+', 2, 2]]
    assert generate_candidate_expressions(['+', 'x', 'y'],
                                {'x': (1, 3), 'y': (1,3)}) == [['+', 1, 1], ['+', 1, 2], ['+', 2, 1], ['+', 2, 2]]


def it_handles_no_variables_all_expressions():
    assert generate_candidate_expressions('+ 1 2') == ['+ 1 2']


def it_removes_whitespace():
    assert remove_whitespace('a    b') == 'a b'
    assert remove_whitespace('a b ') == 'a b'


def it_converts_numeric_strings_to_int():
    assert string_to_int('123') == 123
    assert string_to_int('%abc') == '%abc'


def it_cleans_expressions():
    assert clean_expression('+ 1 2') == ['+', 1, 2]
    assert clean_expression('+ 1     2   x') == ['+', 1, 2, 'x']


def it_identifies_unbalanced_expressions():
    assert expression_is_balanced(['+', 1, 2])
    assert expression_is_balanced(['*', '+', 1, 2, '+', 3, 4])
    assert not expression_is_balanced(['+'])
    assert expression_is_balanced([1])
    assert expression_is_balanced(['+', 'x', 'y'], ['x', 'y'])


def it_identifies_valid_expressions():
    assert expression_is_valid(['+', 'x', 'y'])


def it_evaluates_expressions():
    assert evaluate_expression(['+', 1, 2]) == 3
    assert evaluate_expression(['*', 2, '+', 1, 2]) == 6
    assert evaluate_expression(['+', '+', 1, '*', 2, 3, 4]) == 11
    assert evaluate_expression(['+', '*', '+', 1, 2, 3, 4]) == 13
