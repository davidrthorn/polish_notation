import re


class InvalidNotationException(Exception):
    def __init__(self, rpn_expression: str, message: str):
        msg = f"{message}.\nExpression: '{rpn_expression}'."
        super().__init__(msg)


def validate(rpn_expression: str):
    invalids = re.findall(r"([^\d+\-*/ ])", rpn_expression)
    if invalids:
        raise InvalidNotationException(rpn_expression, f"Invalid characters: '{' '.join(invalids).rstrip()}'")


def _operate(operator: str, a: float, b: float) -> float:
    if operator == "+":
        return a + b
    if operator == "-":
        return a - b
    if operator == "*":
        return a * b
    if operator == "/":
        return a / b


def calculate(rpn_expression: str) -> float:
    validate(rpn_expression)
    stack = rpn_expression.split()
    stack.reverse()
    memory = []

    limit = 100
    while limit > 0 and len(stack):
        current = stack.pop()

        if current not in ["+", "/", "*", "-"]:
            memory.append(float(current))
            continue

        back_one = memory.pop()
        back_two = memory.pop()
        result = _operate(current, back_two, back_one)
        memory.append(result)
        stack = stack + memory

        if len(stack) == 1:
            return stack[0]

        memory = []

        limit -= 1


    # TODO: initial validation (separate function)
    # TODO: the calculation is complete when a single int (the result) remains on the stack
    # TODO: fewer than two operands on the stack when we encounter an operator == Exception

    return 0


