import pytest

from main import calculate, InvalidNotationException


'''
Provided examples
'''


def test_calculate_expression_with_simple_operation_gives_correct_answer():
    assert calculate("3 4 -") == -1


def test_calculate_expression_with_multiple_simple_operations_gives_correct_answer():
    assert calculate("3 4 - 5 +") == 4


def test_calculate_expression_with_multiplication_gives_correct_answer():
    assert calculate("3 4 - 5 *") == -5


def test_calculate_expression_with_more_than_two_sequential_numbers_gives_correct_answer():
    assert calculate("3 4 5 * -") == -17


def test_calculate_expression_with_insufficient_sequential_numbers_throws():
    with pytest.raises(InvalidNotationException):
        calculate("4 + 5")


'''
Additional examples
'''


def test_calculate_expression_with_complex_nesting_gives_correct_answer():
    assert calculate("34567*+8910/11-12")


def test_calculate_empty_string_expression_throws():  # because returning 0 would be misleading
    with pytest.raises(InvalidNotationException):
        calculate("4+5")

