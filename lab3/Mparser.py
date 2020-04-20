#!/usr/`bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
    ("left", '+', '-'),
    ("left", '*', '/'),
    ("left", 'DOTADD', 'DOTSUB'),
    ("left", 'DOTMUL', 'DOTDIV'),
)

variables = {}

def p_error(p):
    if p:
        print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, 0, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""

def p_instructions_opt(p):
    """instructions_opt : instructions
                        | """

def p_instructions_block(p):
    """instructions_block : '{' instructions '}'"""

def p_instructions(p):
    """instructions : instructions instruction
                    | instruction """

def p_instruction(p):
    """instruction : assignment ';'
                   | if_instruction
                   | for_instruction
                   | while_instruction
                   | print_instruction
                   | loop_instruction
                   | return_instruction
                   | instructions_block"""

def p_if_instruction(p):
    """if_instruction : IF '(' relational_expr ')' instructions_block
                      | IF '(' relational_expr ')' instruction
                      | IF '(' relational_expr ')' instructions_block ELSE instruction
                      | IF '(' relational_expr ')' instruction ELSE instruction"""

def p_for_instruction(p):
    """for_instruction : FOR ID '=' INTNUM ':' ID instructions_block
                       | FOR ID '=' INTNUM ':' ID instruction
                       | FOR ID '=' ID ':' ID instructions_block
                       | FOR ID '=' ID ':' ID instruction"""

def p_while_instruction(p):
    """while_instruction : WHILE '(' relational_expr ')' instructions_block
                         | WHILE '(' relational_expr ')' instruction"""

def p_loop_intruction(p):
    """loop_instruction : BREAK ';'
                        | CONTINUE ';' """

def p_return_instruction(p):
    """return_instruction : RETURN expr ';'"""

def p_print_instruction(p):
    """print_instruction : PRINT print_list ';'"""

def p_print_list(p):
    """print_list : print_list ',' expr
                  | print_list ',' STRING 
                  | expr
                  | STRING"""

def p_assignment(p):
    """assignment : ID '=' token
                  | MID '=' elem
                  | ID ADDASSIGN token
                  | ID SUBASSIGN token
                  | ID MULASSIGN token
                  | ID DIVASSIGN token"""
    if p[2] == '=':
        variables[p[1]] = p[3]
    elif p[2] == '+=':
        if p[1] in variables and variables[p[1]] != None:
            variables[p[1]] = variables[p[1]] + p[3]
    elif p[2] == '-=':    
        if p[1] in variables and variables[p[1]] != None:
            variables[p[1]] = variables[p[1]] - p[3]
    elif p[2] == '*=':    
        if p[1] in variables and variables[p[1]] != None:
            variables[p[1]] = variables[p[1]] * p[3]
    elif p[2] == '/=':    
        if p[1] in variables and variables[p[1]] != None:
            variables[p[1]] = variables[p[1]] / p[3]

def p_token_id(p):
    """token : ID"""
    if p[1] in variables:
        p[0]=variables[p[1]]
    else:
        p[0]=0

def p_token(p):
    """token : INTNUM
             | FLONUM
             | matrix
             | expr
             | matrix_expr
             | unary_expr """
    p[0] = p[1]

def p_expr(p):
    """expr : expr '+' term
            | expr '-' term
            | term """
    if len(p) < 3:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]

def p_term(p):
    """term : term '*' factor
            | term '/' factor
            | factor"""
    if len(p) < 3:
        p[0]=p[1]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3]==0:
            p[0] = 0
            print("Error: division by 0")
        else:
            p[0] = p[1] / p[3]

def p_factor(p):
    """factor : '(' expr ')'
              | elem """
    if p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_relational_expr(p):
    """relational_expr : expr GREATEREQUAL expr
                       | expr EQUALS expr 
                       | expr NOTEQUALS expr
                       | expr LOWEREQUAL expr
                       | expr '<' expr
                       | expr '>' expr"""
    if p[2]=='<=':
        p[0] = (p[1] <= p[3])
    elif p[2]=='<':
        p[0] = (p[1] < p[3])
    elif p[2]=='>':
        p[0] = (p[1] > p[3])
    elif p[2]=='>=':
        p[0] = (p[1] > p[3])
    elif p[2]=='==':
        p[0] = (p[1] == p[3])
    elif p[2]=='!=':
        p[0] = (p[1] != p[3])

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

def p_elem_id(p):
    """elem : ID"""
    if p[1] in variables:
        p[0] = variables[p[1]]
    else:
        p[0]=0

def p_elem(p):
    """elem : INTNUM
            | FLONUM"""
    p[0] = p[1]

def p_matrix_expr(p):
    """matrix_expr : matrix_expr DOTADD matrix_term
                   | matrix_expr DOTSUB matrix_term
                   | matrix_term"""

def p_matrix_term(p):
    """matrix_term : matrix_term DOTMUL matrix_factor
                   | matrix_term DOTDIV matrix_factor
                   | matrix_factor"""

def p_matrix_factor(p):
    """matrix_factor : '(' matrix_expr ')'
                     | matrix 
                     | ID """

def p_unary_expr(p):
    """unary_expr : '-' ID
                  | ID \"'\" """ 
    if p[1] == '-':
        if p[2] in variables:
            p[0] = -variables[p[2]]
        else:
            p[0] = 0

parser = yacc.yacc()

