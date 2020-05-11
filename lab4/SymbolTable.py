#!/usr/bin/python


class VariableSymbol:

    def __init__(self, name, type):
        self.name = name
        self.type = type


class VectorSymbol:

    def __init__(self, name, size):
        self.name = name
        self.size = size

class MatrixSymbol:

    def __init__(self, name, size_r, size_c):
        self.name = name
        self.size_r = size_r
        self.size_c = size_c

class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.symbols = {}
        self.parent = parent
        self.name = name
        self.scopes = []

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        return self.symbols[name]

    def getParentScope(self):
        return self.parent

    def pushScope(self, name):
        self.scopes.append(SymbolTable(self, name))

    def popScope(self):
        return self.scopes.pop()


