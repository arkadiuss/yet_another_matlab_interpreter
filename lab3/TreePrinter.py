from __future__ import print_function
import AST


def addToClass(cls):

    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        return get_indent(indent) + self.value + "\n"

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        return get_indent(indent) + self.value + "\n"

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        return get_indent(indent) + self.name + "\n"

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op + "\n"
        res += self.left.printTree(indent+1)
        res += self.right.printTree(indent+1)
        return get_indent(indent) + self.value + "\n"

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        return self.instructions_opt.printTree()

    @addToClass(AST.InstructionsOpt)
    def printTree(self, indent=0):
        return self.instructions.printTree()

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        res = self.instruction.printTree(indent)
        if self.instructions is not None:
            res += self.instructions.printTree(indent)
        return res

    @addToClass(AST.Instruction)
    def printTree(self, indent=0):
        self.instruction.printTree(indent)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body

    # define printTree for other classes
    # ...


def get_indent(indent):
    return "| " * indent
