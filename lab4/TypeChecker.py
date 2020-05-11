#!/usr/bin/python

from SymbolTable import *

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        print(node)
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            print(node)
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):
    def __init__(self):
        self.table = None
        self.types = {
            '+': {
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '-': {
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            },
            '*': {
                'int': {
                    'int': 'int',
                    'float': 'float'
                }
            }, 
            '/': {
                'int': {
                    'int': 'float',
                    'float': 'float'
                }
            }
        }

    def visit_Program(self, node):
        self.table = SymbolTable(None, "")
        self.visit(node.instructions_opt)

    def visit_InstructionsOpt(self, node):
        self.visit(node.instructions)

    def visit_Instructions(self, node):
        self.visit(node.instruction)
        if node.instructions:
            self.visit(node.instructions)

    def visit_Instruction(self, node):
        return self.visit(node.instruction)

    def visit_LoopInstruction(self, node):
        pass

    def visit_ReturnInstruction(self, node):
        pass 

    def visit_BinExpr(self, node):
                                          # alternative usage,
                                          # requires definition of accept method in class Node
        type1 = self.visit(node.left)     # type1 = node.left.accept(self) 
        type2 = self.visit(node.right)    # type2 = node.right.accept(self)
        op    = node.op
        return self.types[op][type1][type2]

    def visit_Outerlist(self, node):
        if(self.outerlist):
            mtype = self.visit(node.outerlist)
            ctype = self.visit(node.innerlist)
            if ctype.size != mtype.c_size:
                print('Incompatibile dimensions')
            return MatrixSymbol(mtype.name, mtype.size_r+1, mtype.size_c)
        ctype = self.visit(node.innerlist)
        return MatrixSymbol('an', 1, ctype.size)

    def visit_Innerlist(self, node):
        if(self.innelist):
            list_type = self.visit(self.innerlist)
            return VectorSymbol(list_type.name, list_type.size + 1)
        return VectorSymbol("an", 1)

    def visit_Vector(self, node):
        return self.visit(node.innerlist)

    def visit_Matrix(self, node):
        return self.visit(node.outerlist)

    def visit_Assignment(self, node):
        pass

    def visit_Variable(self, node):
        return VariableSymbol()
        


