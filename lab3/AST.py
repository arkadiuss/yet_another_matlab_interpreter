class Node(object):
    pass


class IntNum(Node):
    def __init__(self, value):
        self.value = value


class FloatNum(Node):
    def __init__(self, value):
        self.value = value


class Variable(Node):
    def __init__(self, name):
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right):
        self.op = op
        self.left = left
        self.right = right


class Program(Node):
    def __init__(self, instructions_opt):
        self.instructions_opt = instructions_opt


class InstructionsOpt(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction, instructions):
        self.instruction = instruction
        self.instructions = instructions


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class IfInstruction(Node):
    def __init__(self, condition, instructions, else_block):
        self.condition = condition
        self.instructions = instructions
        self.else_block = else_block


class ElseInstruction(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class ForInstruction(Node):
    def __init__(self, variable, start, end, instructions):
        self.variable = variable
        self.start = start
        self.end = end
        self.instructions = instructions


class WhileInstruction(Node):
    def __init__(self, condition, instructions):
        self.condition = condition
        self.instructions = instructions


class PrintInstruction(Node):
    def __init__(self, print_list):
        self.print_list = print_list


class PrintList(Node):
    def __init__(self, print_list, print_expr):
        self.print_list = print_list
        self.print_expr = print_expr


class LoopInstruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class ReturnInstruction(Node):
    def __init__(self, expr):
        self.expr = expr


class Token(Node):
    def __init__(self, token):
        self.token = token


class Expression(Node):
    def __init__(self, expr, sign, term):
        self.expr = expr
        self.sign = sign
        self.term = term


class Mid(Node):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class Matrix(Node):
    def __init__(self, matrix):
        self.matrix = matrix


class Eye(Node):
    def __init__(self, n):
        self.n = n


class Zeros(Node):
    def __init__(self, n):
        self.n = n


class Ones(Node):
    def __init__(self, n):
        self.n = n


class Outerlist(Node):
    def __init__(self, outerlist, innerlist):
        self.outerlist = outerlist
        self.innerlist = innerlist


class Innerlist(Node):
    def __init__(self, innerlist, elem):
        self.innerlist = innerlist
        self.elem = elem


# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
