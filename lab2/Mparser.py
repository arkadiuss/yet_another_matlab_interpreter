#!/usr/`bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   # to fill ...
   ("left", '+', '-'),
   # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, 0, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""

def p_instructions_opt_1(p):
    """instructions_opt : instructions """

def p_instructions_opt_2(p):
    """instructions_opt : """

def p_instructions_block(p):
    """instructions_block : '{' instructions '}'"""

def p_instructions_1(p):
    """instructions : instructions instruction """

def p_instructions_2(p):
    """instructions : instruction """

def p_instruction(p):
    """instruction : assignment ';'
                   | if_instruction"""

def p_if_instruction(p):
    """if_instruction : IF '(' relational_expr ')' instructions_block"""

def p_assignment(p):
    """assignment : ID '=' INTNUM
                  | ID '=' FLONUM
                  | ID '=' matrix
                  | ID '=' expr 
                  | MID '=' INTNUM
                  | ID '=' matrix_expr"""

def p_expr(p):
    """expr : expr '+' term
            | expr '-' term
            | term """

def p_term(p):
    """term : term '*' factor
            | term '/' factor
            | factor"""

def p_factor(p):
    """factor : '(' expr ')'
              | ID """

def p_relational_expr(p):
    """relational_expr : ID GREATEREQUAL INTNUM
                       | ID EQUALS INTNUM 
                       | ID LOWEREQUAL INTNUM  """

def p_MID(p):
    """MID : ID '[' INTNUM ',' INTNUM ']' """

def p_matrix(p):
    """matrix : '[' outerlist ']'
              | ONES '(' INTNUM ')'
              | ZEROS '(' INTNUM ')'
              | EYE '(' INTNUM ')'"""

def p_outerlist(p):
    """outerlist : outerlist ';' innerlist
                 | innerlist"""

def p_innerlist(p):
    """innerlist : innerlist ',' elem
                 | elem"""

def p_elem(p):
    """elem : ID
            | INTNUM
            | FLONUM"""

def p_matrix_expr(p):
    """matrix_expr : matrix_expr DOTADD matrix_term
                   | matrix_expr DOTSUB matrix_term
                   | matrix_term"""

def p_matrix_term(p):
    """matrix_term : matrix_term DOTMUL matrix_factor
                   | matrix_term DOTDIV matrix_factor
                   | matrix_factor"""

def p_matrix_facotr(p):
    """matrix_factor : '(' matrix_expr ')'
                     | ID"""

parser = yacc.yacc()

