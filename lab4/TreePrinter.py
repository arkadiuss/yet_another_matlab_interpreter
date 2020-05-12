from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func

    return decorator


class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.IntNum)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.value) + "\n"

    @addToClass(AST.FloatNum)
    def printTree(self, indent=0):
        return get_indent(indent) + str(self.value) + "\n"

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        return get_indent(indent) + self.name + "\n"

    @addToClass(AST.BinExpr)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op + "\n"
        res += self.left.printTree(indent + 1)
        res += self.right.printTree(indent + 1)
        return res

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
        return self.instruction.printTree(indent)

    @addToClass(AST.IfInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "IF\n"
        res += self.condition.printTree(indent + 1)
        res += get_indent(indent) + "THEN\n"
        res += self.instructions.printTree(indent + 1)
        if self.else_block is not None:
            res += self.else_block.printTree(indent)
        return res

    @addToClass(AST.ElseInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "ELSE\n"
        res += self.instructions.printTree(indent + 1)
        return res

    @addToClass(AST.ForInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "FOR\n"
        res += get_indent(indent + 1) + self.variable + "\n"
        res += get_indent(indent + 1) + "RANGE\n"
        res += get_indent(indent + 2) + str(self.start) + "\n"
        res += get_indent(indent + 2) + (self.end) + "\n"
        res += self.instructions.printTree(indent + 1)
        return res

    @addToClass(AST.WhileInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "WHILE\n"
        res += self.condition.printTree(indent + 1)
        res += self.instructions.printTree(indent + 1)
        return res

    @addToClass(AST.PrintInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "PRINT\n"
        res += self.print_list.printTree(indent+1)
        return res

    @addToClass(AST.ArgsList)
    def printTree(self, indent=0):
        res = self.arg.printTree(indent)
        if self.args_list is not None:
            res += self.args_list.printTree(indent)
        return res

    @addToClass(AST.LoopInstruction)
    def printTree(self, indent=0):
        pass

    @addToClass(AST.ReturnInstruction)
    def printTree(self, indent=0):
        res = get_indent(indent) + "RETURN\n"
        res += self.expr.printTree(indent + 1)
        return res

    @addToClass(AST.Token)
    def printTree(self, indent=0):
        return self.token.printTree(indent)

    @addToClass(AST.Expression)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.sign + "\n"
        res += self.expr.printTree(indent + 1)
        res += self.term.printTree(indent + 1)
        return res

    @addToClass(AST.Mid)
    def printTree(self, indent=0):
        res = get_indent(indent) + "REF\n"
        res += get_indent(indent + 1) + self.id + "\n"
        res += get_indent(indent + 1) + str(self.x) + "\n"
        res += get_indent(indent + 1) + str(self.y) + "\n"
        return res

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        return self.matrix.printTree(indent)
    
    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        res = get_indent(indent) + "VECTOR\n"
        res += self.outerlist.printTree(indent+1)
        return res

    @addToClass(AST.Eye)
    def printTree(self, indent=0):
        res = get_indent(indent) + "EYE\n"
        res += self.n.printTree(indent + 1)
        return res

    @addToClass(AST.Zeros)
    def printTree(self, indent=0):
        res = get_indent(indent) + "ZEROS\n"
        res += self.n.printTree(indent + 1)
        return res

    @addToClass(AST.Ones)
    def printTree(self, indent=0):
        res = get_indent(indent) + "ONES\n"
        res += self.n.printTree(indent + 1)
        return res

    @addToClass(AST.Outerlist)
    def printTree(self, indent=0):
        res = get_indent(indent) + "VECTOR\n"
        res += self.innerlist.printTree(indent+1)
        if self.outerlist is not None:
            res += self.outerlist.printTree(indent)
        return res

    @addToClass(AST.Innerlist)
    def printTree(self, indent=0):
        res = self.elem.printTree(indent)
        if self.innerlist is not None:
            res += self.innerlist.printTree(indent)
        return res
    
    @addToClass(AST.UnaryExpr)
    def printTree(self, indent=0):
        res = get_indent(indent) + self.op + "\n"
        res += self.arg.printTree(indent+1)
        return res

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body


def get_indent(indent):
    return "|  " * indent
