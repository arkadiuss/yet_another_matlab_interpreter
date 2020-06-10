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
            '.*': lambda r1, r2: np.dot(r1, r2),
            './': lambda r1, r2: np.divide(r1, r2)
        }

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Node)
    def visit(self, node):
        print("Unrecognized node: {}".format(node))

    @when(AST.IntNum)
    def visit(self, node):
        return int(node.value)

    @when(AST.FloatNum)
    def visit(self, node):
        return node.value

    @when(AST.String)
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
        r2 = node.right.accept(self)
        if isinstance(node.left, AST.Variable):
            r1 = node.left.name
            self.memory_stack.set(r1, r2)
        else:
            r1 = node.left.id
            matrix = self.memory_stack.get(r1)
            matrix[node.left.x, node.left.y] = r2
            self.memory_stack.set(r1, matrix)
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
        if node.else_block is not None:
            return node.else_block.accept(self)
        return None 

    @when(AST.ElseInstruction)
    def visit(self, node):
        return node.instructions.accept(self)

    @when(AST.ForInstruction)
    def visit(self, node):
        r = None
        self.memory_stack.push(Memory('for_instr'))
        s = node.start.accept(self)
        e = node.end.accept(self)
        for i in range(s, e):
            self.memory_stack.set(node.variable, i)
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
        print(" ".join(map(str, r)))
        return r

    @when(AST.ArgsList)
    def visit(self, node):
        if node.args_list is not None:
            return node.args_list.accept(self) + [node.arg.accept(self)]
        return [node.arg.accept(self)]

    @when(AST.LoopInstruction)
    def visit(self, node):
        if node.instruction == 'break':
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

    @when(AST.Mid)
    def visit(self, node):
        return self.memory_stack.get(node.id.accept(self))[node.x, node.y]

    @when(AST.Matrix)
    def visit(self, node):
        return node.matrix.accept(self)

    @when(AST.Eye)
    def visit(self, node):
        d = node.n.accept(self)[0]
        return np.eye(d)

    @when(AST.Zeros)
    def visit(self, node):
        d = node.n.accept(self)[0]
        return np.zeros((d, d))

    @when(AST.Ones)
    def visit(self, node):
        d = node.n.accept(self)[0]
        return np.ones((d, d))

    @when(AST.Vector)
    def visit(self, node):
        return node.outerlist.accept(self)

    @when(AST.Outerlist)
    def visit(self, node):
        if node.outerlist is None:
            return [node.innerlist.accept(self)]
        outer = node.outerlist.accept(self)
        inner = node.innerlist.accept(self)
        return np.concatenate((outer, [inner]), axis=0)

    @when(AST.Innerlist)
    def visit(self, node):
        if node.innerlist is None:
            return np.array([node.elem.accept(self)])
        return np.concatenate((node.innerlist.accept(self), [node.elem.accept(self)]), axis=None)

    @when(AST.UnaryExpr)
    def visit(self, node):
        if node.op == '-':
            return - node.arg.accept(self)
        return np.transpose(node.arg.accept(self))

    @when(AST.Error)
    def visit(self, node):
        pass
