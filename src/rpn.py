import re


class InvalidNotationException(Exception):
    def __init__(self, rpn_expression: str, message: str):
        msg = f"{message}.\nExpression: '{rpn_expression}'."
        super().__init__(msg)


def validate(rpn_expression: str):
    invalids = re.findall(r"([^\d+\-*/ ])", rpn_expression)
    if invalids:
        raise InvalidNotationException(rpn_expression, f"Invalid characters: '{' '.join(invalids).rstrip()}'")


def calculate(rpn_expression: str) -> int:
    validate(rpn_expression)
    spl = rpn_expression.split()
    # TODO: initial validation (separate function)
    # TODO: the calculation is complete when a single int (the result) remains on the stack
    # TODO: fewer than two operands on the stack when we encounter an operator == Exception

    return 0


