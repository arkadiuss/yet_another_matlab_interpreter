import AST
import SymbolTable
from Memory import *
from Exceptions import *
from visit import *
import sys

sys.setrecursionlimit(10000)


class Interpreter(object):

    def __init__(self):
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
            # TODO operations on matrices
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
        pass

    @when(AST.BinExpr)
    def visit(self, node):
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        return self.bin_expr.get(node.op)(r1, r2)

    @when(AST.Assignment)
    def visit(self, node):
        # TODO add r1 to memory
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
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
        # TODO node.start/end .accept ??
        # TODO node.variable !
        for i in range(node.start, node.end):
            try:
                r = node.instructions.accept(self)
            except BreakException:
                break
            except ContinueException:
                pass
            except ReturnValueException as e:
                return e
        return r

    # simplistic while loop interpretation
    @when(AST.WhileInstruction)
    def visit(self, node):
        r = None
        while node.cond.accept(self):
            try:
                r = node.instructions.accept(self)
            except BreakException:
                return r
            except ContinueException:
                pass
            except ReturnValueException as e:
                return e.value
        return r

    @when(AST.PrintInstruction)
    def visit(self, node):
        return node.print_list.accept(self)

    @when(AST.ArgsList)
    def visit(self, node):
        return node.args_list.accept(self) + node.arg

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
        return node.token.accept(self)

    @when(AST.Expression)
    # TODO w mparserze w ogole tego nie uzywamy
    def visit(self, node):
        pass

    @when(AST.Mid)
    def visit(self, node):
        pass

    @when(AST.Matrix)
    def visit(self, node):
        pass

    @when(AST.Eye)
    def visit(self, node):
        pass

    @when(AST.Zeros)
    def visit(self, node):
        pass

    @when(AST.Ones)
    def visit(self, node):
        pass

    @when(AST.Vector)
    def visit(self, node):
        pass

    @when(AST.Outerlist)
    def visit(self, node):
        pass

    @when(AST.Innerlist)
    def visit(self, node):
        pass

    @when(AST.UnaryExpr)
    def visit(self, node):
        pass

    @when(AST.Error)
    def visit(self, node):
        pass
