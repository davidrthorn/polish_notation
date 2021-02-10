import pytest

from src.rpn import calculate_recursive, InvalidNotationException


def test_calculate_valid_expression_with_simple_operation_returns_correct_result():
    assert calculate_recursive("3 4 -") == -1


def test_calculate_valid_expression_with_multiple_simple_operations_returns_correct_result():
    assert calculate_recursive("3 4 - 5 +") == 4


def test_calculate_valid_expression_with_multiplication_returns_correct_result():
    assert calculate_recursive("3 4 - 5 *") == -5


def test_calculate_valid_expression_with_more_than_two_sequential_numbers_returns_correct_result():
    assert calculate_recursive("3 4 5 * -") == -17


# Fails -- see notes in `src/rpn.py`
def test_calculate_expression_with_complex_nesting_returns_correct_result():
    assert calculate_recursive("5 3 + 10 6 2 / - * 4 +") == 60
