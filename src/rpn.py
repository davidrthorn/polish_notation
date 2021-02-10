from typing import List, Union, Optional

operators = ["+", "/", "*", "-"]


class InvalidNotationException(Exception):
    def __init__(self, message: str, rpn_expression: str = None):
        if rpn_expression:
            message += f"Expression: {rpn_expression}"
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


def _operate(a: float, b: float, operator: str) -> float:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b


# The action is when we hit an operator, apply this thing to the last two things in the array (replace them)
def calculate(rpn_expression: str) -> float:
    stack = to_list(rpn_expression)
    i = 0

    limit = 100
    # TODO: risk of infinity here if something goes wrong
    while len(stack):

        if not limit:
            raise Exception("HIT LIMIT")
        limit -= 1

        if len(stack) == 1:
            return stack[0]

        current = stack[i]
        if current in operators:
            before_this_unit = stack[0:i - 2]
            result_for_this_unit = _operate(stack[i - 2], stack[i - 1], current)
            rest_of_stack = stack[i+1:]

            stack = before_this_unit + [result_for_this_unit] + rest_of_stack
            i = len(before_this_unit) + 1
            continue

        i += 1



    # TODO: initial validation (separate function)
    # TODO: the calculation is complete when a single int (the result) remains on the stack
    # TODO: fewer than two operands on the stack when we encounter an operator == Exception

    return 0


