from typing import List, Union
import re

operators = ["+", "/", "*", "-"]


class InvalidNotationException(Exception):
    def __init__(self, message: str, rpn_expression: str = None):
        if rpn_expression:
            message += f"\nExpression: {rpn_expression}"
        super().__init__(message)


def to_list(rpn_expression: str) -> List[Union[float, str]]:
    if rpn_expression == "":
        raise InvalidNotationException("Expressions cannot be empty strings")

    result = []
    for r in rpn_expression.split():
        if r in operators:
            result.append(r)
            continue
        try:
            result.append(float(r))  # This currently allows the awful expression "False 2.0 +" -- naughty Python!
        except ValueError:
            raise InvalidNotationException(f"'{r}' is not a valid operator or float value")

    return result


def _calculate_unit(a: float, b: float, operator: str) -> float:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b


def calculate(rpn_expression: str) -> float:
    stack = to_list(rpn_expression)

    i = 0
    while len(stack) > 1:

        item = stack[i]
        if item not in operators:
            if i == len(stack) - 1:
                raise InvalidNotationException("Expressions cannot end with a number", rpn_expression)
            i += 1
            continue

        # We've hit an operator, so we should have a calculable unit (this operator and the two previous numbers)

        if i < 2:
            raise InvalidNotationException(
                f"Found an operator not preceded by two or more numbers at position {i}",
                rpn_expression
            )

        operand_1 = stack[i-2]
        operand_2 = stack[i-1]
        operator = item

        result = _calculate_unit(operand_1, operand_2, operator)

        stack_before_unit = stack[0:i-2]
        stack_after_unit = stack[i+1:]

        # Insert the result in place of the unit...
        stack = stack_before_unit + [result] + stack_after_unit  # Replacing our stack every time :(

        # ...and restart iteration from this point
        i = len(stack_before_unit) + 1

    return stack[0]
