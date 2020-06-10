import AST
import SymbolTable
from Memory import *
from Exceptions import *
from visit import *
import sys
import numpy as np

sys.setrecursionlimit(10000)


class Interpreter(object):

    def __init__(self):
        self.memory_stack = MemoryStack(Memory("program"))
        self.bin_expr = {
            '+': lambda r1, r2: r1 + r2,
            '-': lambda r1, r2: r1 - r2,
            '*': lambda r1, r2: r1 * r2,
            '/': lambda r1, r2: r1 / r2,
            '>=': lambda r1, r2: r1 >= r2,
            '==': lambda r1, r2: r1 == r2,
            '!=': lambda r1, r2: r1 != r2,
            '<=': lambda r1, r2: r1 <= r2,
            '<': lambda r1, r2: r1 < r2,
            '>': lambda r1, r2: r1 > r2,
            '.+': lambda r1, r2: r1 + r2,
            '.-': lambda r1, r2: r1 - r2,
            '.*': lambda r1, r2: r1 * r2,
            './': lambda r1, r2: r1 / r2
        }

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Node)
    def visit(self, node):
        print("Unrecognized node: {}".format(node))

    @when(AST.IntNum)
    def visit(self, node):
        return node.value

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.Variable)
    def visit(self, node):
        return self.memory_stack.get(node.name)

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return self.bin_expr.get(node.op)(r1, r2)

    @when(AST.Assignment)
    def visit(self, node):
        r1 = node.left.name  # working for Variable, for MID probably don't
        r2 = node.right.accept(self)
        self.memory_stack.set(r1, r2)
        return r2

    @when(AST.Program)
    def visit(self, node):
        return node.instructions_opt.accept(self)

    @when(AST.InstructionsOpt)
    def visit(self, node):
        return node.instructions.accept(self)

    @when(AST.Instructions)
    def visit(self, node):
        r = node.instruction.accept(self)
        if node.instructions is not None:
            r = node.instructions.accept(self)
        return r

    @when(AST.Instruction)
    def visit(self, node):
        return node.instruction.accept(self)

    @when(AST.IfInstruction)
    def visit(self, node):
        if node.condition.accept(self):
            return node.instructions.accept(self)
        return node.else_block.accept(self)

    @when(AST.ElseInstruction)
    def visit(self, node):
        return node.instructions.accept(self)

    @when(AST.ForInstruction)
    def visit(self, node):
        r = None
        self.memory_stack.push(Memory('for_instr'))
        print(node.start, node.end)
        for i in range(node.start.accept(self), node.end.accept(self)):
            self.memory_stack.set(node.variable.name, i)
            try:
                r = node.instructions.accept(self)
            except BreakException:
                break
            except ContinueException:
                pass
            except ReturnValueException as e:
                self.memory_stack.pop()
                return e.value
        self.memory_stack.pop()
        return r

    # simplistic while loop interpretation
    @when(AST.WhileInstruction)
    def visit(self, node):
        r = None
        self.memory_stack.push(Memory('while_instr'))
        while node.condition.accept(self):
            try:
                r = node.instructions.accept(self)
            except BreakException:
                return r
            except ContinueException:
                pass
            except ReturnValueException as e:
                self.memory_stack.pop()
                return e.value
        self.memory_stack.pop()
        return r

    @when(AST.PrintInstruction)
    def visit(self, node):
        r = node.print_list.accept(self)
        print(r)
        return r

    @when(AST.ArgsList)
    def visit(self, node):
        if node.args_list is not None:
            return node.args_list.accept(self) + self._get_arg_projection(node.arg)
        return self._get_arg_projection(node.arg)

    def _get_arg_projection(self, arg):
        # if isinstance(arg, AST.Variable):
        #     return str(self.memory_stack.get(arg.accept(self)))
        if isinstance(arg, str):
            return arg[1: len(arg)-1]
        return str(arg.accept(self))

    @when(AST.LoopInstruction)
    def visit(self, node):
        if node.instruction == 'BREAK':
            raise BreakException
        raise ContinueException

    @when(AST.ReturnInstruction)
    def visit(self, node):
        r = node.expr.accept(self)
        raise ReturnValueException(r)

    @when(AST.Token)
    def visit(self, node):
        r = node.token.accept(self)
        return r

    @when(AST.Expression)
    # TODO w mparserze w ogole tego nie uzywamy
    def visit(self, node):
        pass

    @when(AST.Mid)
    def visit(self, node):
        # TODO
        pass

    @when(AST.Matrix)
    def visit(self, node):
        return node.matrix.accept(self)

    @when(AST.Eye)
    def visit(self, node):
        return np.eye(node.n.accept(self))

    @when(AST.Zeros)
    def visit(self, node):
        return np.zeros(node.n.accept(self))

    @when(AST.Ones)
    def visit(self, node):
        return np.ones(node.n.accept(self))

    @when(AST.Vector)
    def visit(self, node):
        return node.outerlist.accept(self)

    @when(AST.Outerlist)
    def visit(self, node):
        return np.concatenate(([node.outerlist.accept(self)], [node.innerlist.accept(self)]), axis=1)

    @when(AST.Innerlist)
    def visit(self, node):
        return np.concatenate((node.innerlist.accept(self), node.elem.accept(self)), axis=0)

    @when(AST.UnaryExpr)
    def visit(self, node):
        if node.op == '-':
            return - node.arg.accept(self)
        return np.transpose(node.arg.accept(self))

    @when(AST.Error)
    def visit(self, node):
        pass
