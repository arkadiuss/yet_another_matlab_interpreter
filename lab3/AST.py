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
    def __init__(self, instructions, instruction):
        self.instructions = instructions
        self.instruction = instruction


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


# TODO nwm czy nie lepiej bedzie to podzielic w MParserze na osobne przypadki
# class IfInstruction(Node):
#     def __init__(self):


# | for_instruction
# | while_instruction
# | print_instruction
# | loop_instruction
# | return_instruction
# | instructions_block

# ...
# fill out missing classes
# ...

class Error(Node):
    def __init__(self):
        pass
