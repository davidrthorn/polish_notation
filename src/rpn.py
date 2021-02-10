from typing import List, Union

operators = ["+", "/", "*", "-"]


class InvalidNotationException(Exception):
    def __init__(self, message: str, rpn_expression: str = None):
        if rpn_expression:
            message += f"\nExpression: {rpn_expression}"
        super().__init__(message)


def to_list(rpn_expression: str) -> List[Union[float, str]]:
    result = []
    for r in rpn_expression.split():
        if r in operators:
            result.append(r)
            continue
        try:
            # TODO: how liberal is float? What will it do with False for example?
            result.append(float(r))
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
            i += 1
            continue

        # We've hit an operator, so we should have a calculable unit (this operator and the two previous numbers)
        a_index = i-2
        b_index = i-1

        if a_index < 0 or b_index < 0:
            raise InvalidNotationException(
                f"Found an operator not preceded by two or more numbers at position {i}",
                rpn_expression
            )

        operand_1 = stack[a_index]
        operand_2 = stack[b_index]

        operator = item
        result = _calculate_unit(operand_1, operand_2, operator)

        stack_before_unit = stack[0:i-2]
        stack_after_unit = stack[i+1:]

        # Insert the result in place of the unit...
        stack = stack_before_unit + [result] + stack_after_unit

        # ...and restart iteration from this point
        i = len(stack_before_unit) + 1

    return stack[0]
