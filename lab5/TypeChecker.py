#!/usr/bin/python

from SymbolTable import *
import AST

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
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
        self.scope = SymbolTable(None, "Program")
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
            },
            '=': {
                
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

    def visit_ForInstruction(self, node):
        self.scope.pushScope('Loop')
        self.visit(node.instructions)
        self.scope.popScope()

    def visit_WhileInstruction(self, node):
        self.scope.pushScope('Loop')
        self.visit(node.instructions)
        self.scope.popScope()

    def visit_IfInstruction(self, node):
        self.scope.pushScope('If')
        self.visit(node.instructions)
        self.scope.popScope()
    
    def visit_LoopInstruction(self, node):
        if not self.scope.isUnderScope('Loop'):
            print("[{}] Break or coninue outer the Loop scope".format(node.lineno))
        pass

    def visit_ReturnInstruction(self, node):
        if not self.scope.isUnderScope('Function'):
            print("[{}] Return used outside the function scope".format(node.lineno))
        pass 
    
    def visit_PrintInstruction(self, node):
        pass

    def visit_BinExpr(self, node):
        type1 = self.visit(node.left)
        type2 = self.visit(node.right) 
        op    = node.op
        if isinstance(type1, VariableSymbol):
            type1 = type1.type
        if isinstance(type2, VariableSymbol):
            type2 = type2.type
            
        if isinstance(type1, MatrixSymbol) and isinstance(type2, MatrixSymbol):
            if op == '.*' and type1.size_c == type2.size_r:
                return MatrixSymbol(type1.size_r, type2.size_c)
            if op == './' and type2.size_c == type2.size_r and type1.size_c == type2.size_c: 
                return MatrixSymbol(type1.size_r, type2.size_c)
            if op in ['.+', '.-'] and type1.size_r == type2.size_r and type1.size_c == type2.size_c:
                return MatrixSymbol(type1.size_r, type2.size_c)
        if isinstance(type1, str) and isinstance(type2, str):
            return self.types[op][type1][type2] 
        print("[{0}] Incompatibile types: {1} and {2}".format(node.lineno, type1, type2))


    def visit_Outerlist(self, node):
        if node.outerlist:
            mtype = self.visit(node.outerlist)
            ctype = self.visit(node.innerlist)
            # print(node.lineno)
            if ctype.size != mtype.size_c:
                print('[{}] Incompatibile dimensions'.format(node.lineno))
            return MatrixSymbol(mtype.size_r+1, mtype.size_c)
        ctype = self.visit(node.innerlist)
        return MatrixSymbol(1, ctype.size)

    def visit_Innerlist(self, node):
        if node.innerlist:
            list_type = self.visit(node.innerlist)
            return VectorSymbol(list_type.size + 1)
        return VectorSymbol(1)

    def visit_Vector(self, node):
        vector = self.visit(node.innerlist)
        return MatrixSymbol(1, vector.size)

    def visit_Matrix(self, node):
        return self.visit(node.matrix)

    def visit_Zeros(self, node):
        atype = self.visit(node.n)
        if len(atype) == 0 or len(atype) > 1 or atype[0] != 'int':
            print("[{}] Zeros accepts exactly one argument of type int".format(node.lineno))
            return None
        n = node.n.arg.token.value
        return MatrixSymbol(n,n)

    def visit_Ones(self, node):
        atype = self.visit(node.n)
        if len(atype) == 0 or len(atype) > 1 or atype[0] != 'int':
            print("[{}] Ones accepts exactly one argument of type int".format(node.lineno))
            return None
        n = node.n.arg.token.value
        return MatrixSymbol(n,n)


    def visit_Eye(self, node):
        atype = self.visit(node.n)
        if len(atype) == 0 or len(atype) > 1 or atype[0] != 'int':
            print("[{}] Eye accepts exactly one argument of type int".format(node.lineno))
            return None
        n = node.n.arg.token.value
        return MatrixSymbol(n,n)

    def visit_Assignment(self, node):
        rtype = self.visit(node.right)
        if isinstance(node.left, AST.Variable):
            symbol = VariableSymbol(node.left.name, rtype)
            self.scope.put(node.left.name, symbol)
        else:
            symbol = VariableSymbol(node.left.id, rtype)
        return symbol

    def visit_Variable(self, node):
        return self.scope.get(node.name)
        
    def visit_Token(self, node):
        return self.visit(node.token)

    def visit_ArgsList(self, node):
        argtype = self.visit(node.arg)
        if node.args_list:
            return [ argtype ] + self.visit(node.args_list)
        return [ argtype ]

    def visit_IntNum(self, node):
        return 'int'

    def visit_FloatNum(self, node):
        return 'float'

    def visit_String(self, node):
        return 'string'

