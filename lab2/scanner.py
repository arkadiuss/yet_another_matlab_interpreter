import ply.lex as lex

reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'while': 'WHILE',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'return',
    'eye': 'EYE',
    'zeros': 'ZEROS',
    'ones': 'ONES',
    'print': 'PRINT'
}

tokens = [
    'ID',
    'FLONUM',
    'INTNUM',
    'STRING',
    'DOTADD',
    'DOTSUB',
    'DOTMUL',
    'DOTDIV',
    'ADDASSIGN',
    'SUBASSIGN',
    'MULASSIGN',
    'DIVASSIGN',
    'GREATEREQUAL',
    'LOWEREQUAL',
    'EQUALS',
    'NOTEQUALS',
    'COMMENT'
]
tokens += list(reserved.values())

literals = "+-*/=();,':[]{}<>"

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_FLONUM(t):
    r'\d*\.\d+[eE]\d+|\d+\.\d*|\d*\.\d+'
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[^"]*\"'
    return t

def t_COMMENT(t):
    r'\#[^\n]*'
    pass

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'
t_ADDASSIGN = r'\+='
t_SUBASSIGN = r'\-='
t_MULASSIGN = r'\*='
t_DIVASSIGN = r'\/='
t_GREATEREQUAL = '>='
t_LOWEREQUAL = '<='
t_EQUALS = '=='
t_NOTEQUALS = '!='

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

lexer = lex.lex()
