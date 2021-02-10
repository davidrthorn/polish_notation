import pytest

from main import calculate, InvalidNotationException


'''
Provided examples
'''


def test_calculate_expression_with_simple_operation_gives_correct_answer():
    assert calculate("34-") == -1


def test_calculate_expression_with_multiple_simple_operations_gives_correct_answer():
    assert calculate("34-5+") == 4


def test_calculate_expression_with_multiplication_gives_correct_answer():
    assert calculate("34-5*") == -5


def test_calculate_expression_with_more_than_two_sequential_numbers_gives_correct_answer():
    assert calculate("345*-") == -17


def test_calculate_expression_with_insufficient_sequential_numbers_throws():
    with pytest.raises(InvalidNotationException):
        calculate("4+5")

