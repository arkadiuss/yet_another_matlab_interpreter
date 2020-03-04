import ply.lex as lex

tokens = (
    'ID',
    'INTNUM',
    'ZEROS',
    'ONES',
    'EYE',
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
    'NOTEQUALS'
)

literals = "+-*/=();,':[]{}<>"

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_INTNUM(t):
    r'[\d+]'
    t.value = int(t.value)
    return t

t_DOTADD = '.+'
t_DOTSUB = '.-'
t_DOTMUL = '.*'
t_DOTDIV = '/*'
t_ADDASSIGN = '+='
t_SUBASSIGN = '-='
t_MULASSIGN = '*='
t_DIVASSIGN = '/='
t_GREATEREQUAL = '>='
t_LOWEREQUAL = '<='
t_EQUALS = '=='
t_NOTEQUALS = '!='

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexel.lineno += len(t.value)

lexer = lex.lex()

def find_column(text, token):
    return -1
