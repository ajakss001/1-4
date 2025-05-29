from enum import Enum

class MathOp(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'

def calculate(a, b, op):
    actions = {
        MathOp.ADD: a + b,
        MathOp.SUB: a - b,
        MathOp.MUL: a * b,
        MathOp.DIV: a / b if b != 0 else 'Error'
    }
    return a, b, op.value, actions.get(op, 'Unknown operation')

print(calculate(10, 5, MathOp.ADD))
print(calculate(10, 0, MathOp.DIV))