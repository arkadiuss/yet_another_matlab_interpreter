#!/usr/`bin/python

import scanner
import ply.yacc as yacc
from AST import *

tokens = scanner.tokens

precedence = (
    ("left", '-', "'"),
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
    p[0] = Program(p[1])

def p_instructions_opt(p):
    """instructions_opt : instructions"""
    p[0] = InstructionsOpt(p[1])

def p_instructions_block(p):
    """instructions_block : '{' instructions '}'"""
    p[0] = Instructions(p[2], None)

def p_instructions(p):
    """instructions : instruction instructions
                    | instruction """
    p[0] = Instructions(p[1], p[2]) if len(p) == 3 else Instructions(p[1], None)

def p_instruction_1(p):
    """instruction : assignment ';'
                   | if_instruction
                   | for_instruction
                   | while_instruction
                   | print_instruction
                   | loop_instruction
                   | return_instruction
                   | instructions_block"""
    p[0] = Instruction(p[1])

def p_if_instruction_1(p):
    """if_instruction : IF '(' relational_expr ')' instructions_block
                      | IF '(' relational_expr ')' instruction"""
    p[0] = IfInstruction(p[3], p[5], None)

def p_if_instruction_2(p):
    """if_instruction : IF '(' relational_expr ')' instructions_block ELSE instruction
                      | IF '(' relational_expr ')' instruction ELSE instruction"""
    p[0] = IfInstruction(p[3], p[5], ElseInstruction(p[7]))

def p_for_instruction(p):
    """for_instruction : FOR ID '=' INTNUM ':' ID instructions_block
                       | FOR ID '=' INTNUM ':' ID instruction
                       | FOR ID '=' ID ':' ID instructions_block
                       | FOR ID '=' ID ':' ID instruction"""
    p[0] = ForInstruction(p[2], p[4], p[6], p[7])

def p_while_instruction(p):
    """while_instruction : WHILE '(' relational_expr ')' instructions_block
                         | WHILE '(' relational_expr ')' instruction"""
    p[0] = WhileInstruction(p[3], p[5])

def p_loop_intruction(p):
    """loop_instruction : BREAK ';'
                        | CONTINUE ';' """
    p[0] = LoopInstruction(p[1])

def p_return_instruction(p):
    """return_instruction : RETURN expr ';'"""
    p[0] = ReturnInstruction(p[2])

def p_print_instruction(p):
    """print_instruction : PRINT args_list ';'"""
    p[0] = PrintInstruction(p[2])

def p_args_list_1(p):
    """args_list : args_list ',' expr
                  | args_list ',' STRING"""
    p[0] = ArgsList(p[1], p[3])

def p_args_list_2(p):
    """args_list : expr
                  | STRING"""
    p[0] = ArgsList(None, p[1])

def p_assignment_1(p):
    """assignment : ID '=' token
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
    p[0] = BinExpr(p[2], Variable(p[1]), p[3])

def p_assignment_2(p):
    """assignment : MID '=' elem"""
    variables[p[1]] = p[3]
    p[0] = BinExpr(p[2], p[1], p[3])

def p_token_id(p):
    """token : ID"""
    if p[1] in variables:
        #p[0]=variables[p[1]]
        p[0] = Token(p[1])
    else:
        p[0] = Token(0)

def p_token(p):
    """token : int
             | float
             | matrix
             | expr
             | matrix_expr
             | unary_expr """
    p[0] = Token(p[1])

def p_expr(p):
    """expr : expr '+' term
            | expr '-' term
            | term """
    if len(p) < 3:
        p[0] = p[1]
    elif p[2] == '+':
        #p[0] = p[1] + p[3]
        p[0] = BinExpr(p[2], p[1], p[3])
    elif p[2] == '-':
        #p[0] = p[1] - p[3]
        p[0] = BinExpr(p[2], p[1], p[3])

def p_term(p):
    """term : term '*' factor
            | term '/' factor
            | factor"""
    if len(p) < 3:
        p[0]=p[1]
    elif p[2] == '*':
        # p[0] = p[1] * p[3]
        p[0] = BinExpr(p[2], p[1], p[3])
    elif p[2] == '/':
        if p[3]==0:
            p[0] = 0
            #p[0] = BinExpr(p[2], p[1], p[3])
            print("Error: division by 0")
        else:
            #p[0] = p[1] / p[3]
            p[0] = BinExpr(p[2], p[1], p[3])

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
    #if p[2]=='<=':
    #    p[0] = (p[1] <= p[3])
    #elif p[2]=='<':
    #    p[0] = (p[1] < p[3])
    #elif p[2]=='>':
    #    p[0] = (p[1] > p[3])
    #elif p[2]=='>=':
    #    p[0] = (p[1] > p[3])
    #elif p[2]=='==':
    #    p[0] = (p[1] == p[3])
    #elif p[2]=='!=':
    #    p[0] = (p[1] != p[3])
    p[0] = BinExpr(p[2], p[1], p[3])

def p_MID(p):
    """MID : ID '[' INTNUM ',' INTNUM ']' """
    p[0] = Mid(p[1], p[3], p[5])

def p_matrix_1(p):
    # for working opers.m
    """matrix : '[' outerlist ']' """
    # for working init.m
    #"""matrix : '[' outerlist ';' ']' """
    p[0]=Matrix(p[2])

def p_matrix_2(p):
    """matrix : ONES '(' args_list ')'"""
    p[0]=Matrix(Ones(p[3]))
    
def p_matrix_3(p):
    """matrix : ZEROS '(' args_list ')'"""
    p[0]=Matrix(Zeros(p[3]))

def p_matrix_4(p):
    """matrix : EYE '(' args_list ')'"""
    p[0]=Matrix(Eye(p[3]))

def p_vector(p):
    """vector : '[' innerlist ']'"""
    p[0]=Vector(p[2])

def p_outerlist_1(p):
     """outerlist : outerlist ';' innerlist"""
     p[0] = Outerlist(p[1], p[3])

def p_outerlist_2(p):
    """outerlist : innerlist """
    p[0] = Outerlist(None, p[1])

def p_innerlist_1(p):
    """innerlist : innerlist ',' elem"""
    p[0] = Innerlist(p[1], p[3])

def p_innerlist_2(p):
    """innerlist : elem"""
    p[0] = Innerlist(None, p[1])

def p_innerlist_3(p):
    """innerlist : """
    p[0] = Innerlist(None, None)

def p_elem_id(p):
    """elem : ID"""
    #if p[1] in variables:
    #    p[0] = variables[p[1]]
    #else:
    #    p[0]=0
    p[0] = Variable(p[1])

def p_elem(p):
    """elem : int
            | float"""
    p[0] = Token(p[1])

def p_matrix_expr(p):
    """matrix_expr : matrix_expr DOTADD matrix_term
                   | matrix_expr DOTSUB matrix_term
                   | matrix_term"""
    if len(p) > 2:
        p[0] = BinExpr(p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_matrix_term(p):
    """matrix_term : matrix_term DOTMUL matrix_factor
                   | matrix_term DOTDIV matrix_factor
                   | matrix_factor"""
    if len(p) > 2:
        p[0] = BinExpr(p[2], p[1], p[3])
    else:
        p[0] = p[1]

def p_matrix_factor_1(p):
    """matrix_factor : '(' matrix_expr ')'
                     | matrix""" 
    if p[1] == '(':
        p[0]=p[2]
    else:
        p[0]=p[1]

def p_matrix_factor_2(p):
    """matrix_factor : ID""" 
    p[0]=Variable(p[1])

def p_unary_expr(p):
    """unary_expr : '-' expr
                  | matrix_expr \"'\" """ 
    if p[1] == '-':
        #if p[2] in variables:
        #    p[0] = -variables[p[2]]
        #else:
        #    p[0] = 0
        p[0] = UnaryExpr('-', Variable(p[2]))
    else:
        p[0] = UnaryExpr("'", p[1])

def p_int(p):
    """int : INTNUM """
    p[0] = IntNum(p[1])

def p_float(p):
    """float : FLONUM"""
    p[0] = FloatNum(p[1])


parser = yacc.yacc()

