import pytest

from src.rpn import calculate, InvalidNotationException, to_list


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


def test_calculate_expression_with_insufficient_sequential_numbers_after_valid_sequence_throws():
    with pytest.raises(InvalidNotationException):
        calculate("1 2 - 4 + 5")


def test_to_list_returns_list_of_floats_and_symbols_when_input_valid():
    assert to_list("1 2 +") == [1.0, 2.0, '+']


def test_calculate_expression_with_complex_nesting_gives_correct_answer():
    assert calculate("5 3 + 10 6 2 / - * 4 +") == 60  # (5 + 3) * (10 - (6 / 2)) + 4 == 60


def test_calculate_expression_with_decimals_returns_correct_result():
    assert calculate("1.2 2 /") == 0.6


def test_calculate_expression_with_negative_number_gives_correct_answer():
    assert calculate("-2 10 *") == -20


def test_calculate_ignores_whitespace_padding():
    assert calculate(" 1 2 + ") == 3


def test_calculate_empty_string_expression_throws():  # because returning 0 would be misleading
    with pytest.raises(InvalidNotationException):
        calculate("")


def test_calculate_expression_with_invalid_chars_throws():
    with pytest.raises(InvalidNotationException) as e:
        calculate("34 + B")
    assert "Invalid characters: 'B'" in str(e.value)


# TODO: The exception thrown here should be informative
def test_calculate_expression_without_delimiters_throws():  # because without delimiters, notation is ambiguous
    with pytest.raises(InvalidNotationException):
        calculate("12-")
