from typing import List, Union

operators = ["+", "-", "*", "/"]


class InvalidNotationException(Exception):
    def __init__(self, message: str = "Expression could not be processed", rpn_expression: str = None):
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
            result.append(float(r))
        except ValueError:
            raise InvalidNotationException(f"'{r}' is not a valid operator or float value")

    return result


def calculate_unit(a: float, b: float, operator: str) -> float:
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

        try:
            item = stack[i]
        except IndexError:
            raise InvalidNotationException(rpn_expression=rpn_expression)

        if item not in operators:
            i += 1
            continue

        # We've hit an operator, so we should have a calculable unit (this operator and the two previous numbers)
        operand_1 = stack[i-2]
        operand_2 = stack[i-1]
        operator = item

        if not isinstance(operand_1, float) or not isinstance(operand_2, float):
            raise InvalidNotationException(rpn_expression=rpn_expression)

        result = calculate_unit(operand_1, operand_2, operator)

        stack_before_unit = stack[0:i-2]
        stack_after_unit = stack[i+1:]

        # Insert the result in place of the unit...
        stack = stack_before_unit + [result] + stack_after_unit  # Replacing our stack every time :(

        # ...and restart iteration from this point
        i = len(stack_before_unit) + 1

    answer = stack[0]
    if not isinstance(answer, float):
        raise InvalidNotationException(f"Answer was '{answer}', which is not a valid float", rpn_expression=rpn_expression)

    return answer


'''
BONUS RECURSIVE IMPLEMENTATION (that doesn't quite work -- see test_recursive.py)

The problem I have not solved looks like this:

Every RPN expression is composed of an operator and two valid RPN expressions, where a number
is considered valid.

We also know that every valid RPN expression ends with an operator.

Hence, we know that every RPN expression can be evaluated by applying its final operator to the
two operands preceding it...

...if we can figure out what those operands are. We need to be able to split any string preceding
the final operand into two operands that can, in turn, be evaluated. I thought I'd achieved this here,
but the complex case ('5 3 + 10 6 2 / - * 4 +') still fails. The implementation here cannot deal with
the fact that the first operand in that case is '5 3 +'. that is to say, it can't deal with there being
two operands that are themselves non-numerical RPN expressions. It doesn't know (right now) where to
split things up.
'''


def calculate_recursive(rpn_expression):
    return _calculate_recursive(to_list(rpn_expression))


def _calculate_recursive(data):
    operator = data[-1]
    if len(data) == 3:
        return calculate_unit(data[-3], data[-2], operator)
    if isinstance(data[-2], float):
        return calculate_unit(_calculate_recursive(data[0:-2]), data[-2], operator)
    return calculate_unit(data[0], _calculate_recursive(data[1:-1]), operator)


