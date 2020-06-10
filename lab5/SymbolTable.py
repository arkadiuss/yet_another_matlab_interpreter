#!/usr/bin/python


class VariableSymbol:

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __str__(self):
        return "{0} of type {1}".format(self.name, self.type)

class VectorSymbol:

    def __init__(self, size):
        self.size = size

    def __str__(self):
        return "vector of size {0}".format(self.size)

class MatrixSymbol:

    def __init__(self, size_r, size_c):
        self.size_r = size_r
        self.size_c = size_c

    def __str__(self):
        return "matrix {0}x{1}".format(self.size_r, self.size_c)

class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.symbols = {}
        self.parent = parent
        self.name = name
        self.scopes = [ "program" ]

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol
        print("put", self.symbols)

    def get(self, name): # get variable symbol or fundef from <name> entry
        print("get", self.symbols)
        return self.symbols[name]

    def getParentScope(self):
        return self.scopes[-1]

    def isUnderScope(self, name):
        for s in reversed(self.scopes):
            if s == name:
                return True
        return False

    def pushScope(self, name):
        self.scopes.append(name)

    def popScope(self):
        return self.scopes.pop()


