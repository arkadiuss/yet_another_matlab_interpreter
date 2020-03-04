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
    'DOTDIV'
)

literals = "+-*/=();"

def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

def t_INTNUM(t):
    r'[\d+]'
    t.value = int(t.value)
    return t

def t_ZEROS(t):
    r'zeros'

def t_ONES(t):
    r'ones'

def t_EYE(t):
    r'eye'

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexel.lineno += len(t.value)

lexer = lex.lex()

def find_column(text, token):
    return -1
