class Node(object):
    def __init__(self, lineno):
        self.lineno = lineno


class IntNum(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value


class FloatNum(Node):
    def __init__(self, value, lineno):
        super().__init__(lineno)
        self.value = value


class Variable(Node):
    def __init__(self, name, lineno):
        super().__init__(lineno)
        self.name = name


class BinExpr(Node):
    def __init__(self, op, left, right, lineno):
        super().__init__(lineno)
        self.op = op
        self.left = left
        self.right = right

class Assignment(Node):
    def __init__(self, op, left, right, lineno):
        super().__init__(lineno)
        self.op = op
        self.left = left
        self.right = right

class Program(Node):
    def __init__(self, instructions_opt, lineno):
        super().__init__(lineno)
        self.instructions_opt = instructions_opt


class InstructionsOpt(Node):
    def __init__(self, instructions, lineno):
        super().__init__(lineno)
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instruction, instructions, lineno):
        super().__init__(lineno)
        self.instruction = instruction
        self.instructions = instructions


class Instruction(Node):
    def __init__(self, instruction, lineno):
        super().__init__(lineno)
        self.instruction = instruction


class IfInstruction(Node):
    def __init__(self, condition, instructions, else_block, lineno):
        super().__init__(lineno)
        self.condition = condition
        self.instructions = instructions
        self.else_block = else_block


class ElseInstruction(Node):
    def __init__(self, instructions, lineno):
        super().__init__(lineno)
        self.instructions = instructions


class ForInstruction(Node):
    def __init__(self, variable, start, end, instructions, lineno):
        super().__init__(lineno)
        self.variable = variable
        self.start = start
        self.end = end
        self.instructions = instructions


class WhileInstruction(Node):
    def __init__(self, condition, instructions, lineno):
        super().__init__(lineno)
        self.condition = condition
        self.instructions = instructions


class PrintInstruction(Node):
    def __init__(self, print_list, lineno):
        super().__init__(lineno)
        self.print_list = print_list


class ArgsList(Node):
    def __init__(self, args_list, arg, lineno):
        super().__init__(lineno)
        self.args_list = args_list
        self.arg = arg

class LoopInstruction(Node):
    def __init__(self, instruction, lineno):
        super().__init__(lineno)
        self.instruction = instruction
        
class ReturnInstruction(Node):
    def __init__(self, expr, lineno):
        super().__init__(lineno)
        self.expr = expr


class Token(Node):
    def __init__(self, token, lineno):
        super().__init__(lineno)
        self.token = token


class Expression(Node):
    def __init__(self, expr, sign, term, lineno):
        super().__init__(lineno)
        self.expr = expr
        self.sign = sign
        self.term = term


class Mid(Node):
    def __init__(self, id, x, y, lineno):
        super().__init__(lineno)
        self.id = id
        self.x = x
        self.y = y


class Matrix(Node):
    def __init__(self, matrix, lineno):
        super().__init__(lineno)
        self.matrix = matrix


class Eye(Node):
    def __init__(self, n, lineno):
        super().__init__(lineno)
        self.n = n


class Zeros(Node):
    def __init__(self, n, lineno):
        super().__init__(lineno)
        self.n = n


class Ones(Node):
    def __init__(self, n, lineno):
        super().__init__(lineno)
        self.n = n

class Vector(Node):
    def __init__(self, outerlist, lineno):
        super().__init__(lineno)
        self.outerlist = outerlist

class Outerlist(Node):
    def __init__(self, outerlist, innerlist, lineno):
        super().__init__(lineno)
        self.outerlist = outerlist
        self.innerlist = innerlist


class Innerlist(Node):
    def __init__(self, innerlist, elem, lineno):
        super().__init__(lineno)
        self.innerlist = innerlist
        self.elem = elem

class UnaryExpr(Node):
    def __init__(self, op, arg, lineno):
        super().__init__(lineno)
        self.op = op
        self.arg = arg

class Error(Node):
    def __init__(self, lineno):
        super().__init__(self, lineno)
