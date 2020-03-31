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

def p_token(p):
    """token : ID
             | INTNUM
             | FLONUM
             | matrix
             | expr
             | matrix_expr
             | unary_expr """

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
              | elem """

def p_relational_expr(p):
    """relational_expr : expr GREATEREQUAL expr
                       | expr EQUALS expr 
                       | expr NOTEQUALS expr
                       | expr LOWEREQUAL expr
                       | expr '<' expr
                       | expr '>' expr"""

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

def p_matrix_factor(p):
    """matrix_factor : '(' matrix_expr ')'
                     | matrix_elem"""

def p_unary_expr(p):
    """unary_expr : '-' ID
                  | ID \"'\" """ 

def p_matrix_elem(p):
    """matrix_elem : ID
                   | matrix"""

parser = yacc.yacc()

