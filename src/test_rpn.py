import pytest

from src.rpn import calculate, InvalidNotationException

'''
Provided examples
'''


def test_calculate_valid_expression_with_simple_operation_returns_correct_result():
    assert calculate("3 4 -") == -1


def test_calculate_valid_expression_with_multiple_simple_operations_returns_correct_result():
    assert calculate("3 4 - 5 +") == 4


def test_calculate_valid_expression_with_multiplication_returns_correct_result():
    assert calculate("3 4 - 5 *") == -5


def test_calculate_valid_expression_with_more_than_two_sequential_numbers_returns_correct_result():
    assert calculate("3 4 5 * -") == -17


def test_calculate_valid_expression_with_insufficient_sequential_numbers_raises():
    with pytest.raises(InvalidNotationException):
        calculate("4 + 5")


'''
Additional examples
'''


def test_calculate_expression_with_single_number_returns_correct_result():
    assert calculate("5") == 5


def test_calculate_expression_with_complex_nesting_returns_correct_result():
    assert calculate("5 3 + 10 6 2 / - * 4 +") == 60


def test_calculate_expression_with_decimals_returns_correct_result():
    assert calculate("1.2 2 /") == 0.6


def test_calculate_expression_with_negative_number_returns_correct_result():
    assert calculate("-2 10 *") == -20


def test_calculate_invalid_expression_with_insufficient_sequential_numbers_after_valid_sequence_raises():
    with pytest.raises(InvalidNotationException):
        calculate("1 2 - 4 + 5")


def test_calculate_invalid_expression_with_too_many_sequential_numbers_after_valid_sequence_raises():
    with pytest.raises(InvalidNotationException):
        calculate("1 2 - 4 4 4 4 +")


def test_calculate_invalid_expression_with_invalid_operator_sequence_raises():
    with pytest.raises(InvalidNotationException):
        calculate("1 2 - 4 + -")


def test_calculate_ignores_whitespace_padding():
    assert calculate(" 1 2 + ") == 3


def test_calculate_empty_string_expression_raises():  # because returning 0 would be misleading
    with pytest.raises(InvalidNotationException):
        calculate("")


def test_calculate_invalid_expression_with_invalid_chars_raises():
    with pytest.raises(InvalidNotationException) as e:
        calculate("34 B +")
    assert "'B'" in str(e.value)


def test_calculate_invalid_expression_without_delimiters_raises():  # because without delimiters, notation is ambiguous
    with pytest.raises(InvalidNotationException):
        calculate("12-")


def test_calculate_invalid_expression_with_spaces_without_delimiters_raises():
    with pytest.raises(InvalidNotationException):
        calculate("12- 4 +")
