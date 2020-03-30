
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left+-ADDASSIGN BREAK COMMENT CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQUALS EYE FLONUM GREATEREQUAL ID IF INTNUM LOWEREQUAL MULASSIGN NOTEQUALS ONES PRINT STRING SUBASSIGN THEN WHILE ZEROS returnprogram : instructions_optinstructions_opt : instructions instructions_opt : instructions_block : '{' instructions '}'instructions : instructions instruction instructions : instruction instruction : assignment ';'\n                   | if_instructionif_instruction : IF '(' relational_expr ')' instructions_blockassignment : ID '=' INTNUM\n                  | ID '=' FLONUM\n                  | ID '=' matrix\n                  | ID '=' expr \n                  | MID '=' INTNUMexpr : expr '+' term\n            | expr '-' term\n            | term term : term '*' factor\n            | term '/' factor\n            | factorfactor : '(' expr ')'\n              | ID relational_expr : ID GREATEREQUAL INTNUM\n                       | ID EQUALS INTNUM \n                       | ID LOWEREQUAL INTNUM  MID : ID '[' INTNUM ',' INTNUM ']' matrix : '[' outerlist ']'\n              | ONES '(' INTNUM ')'\n              | ZEROS '(' INTNUM ')'\n              | EYE '(' INTNUM ')'outerlist : outerlist ';' innerlist\n                 | innerlistinnerlist : innerlist ',' elem\n                 | elemelem : ID\n            | INTNUM\n            | FLONUM"
    
_lr_action_items = {'$end':([0,1,2,3,4,6,10,11,63,75,],[-3,0,-1,-2,-6,-8,-5,-7,-9,-4,]),'ID':([0,3,4,6,10,11,12,15,21,23,32,33,44,45,54,55,63,64,74,75,],[7,7,-6,-8,-5,-7,16,31,37,16,16,16,16,16,37,37,-9,7,7,-4,]),'IF':([0,3,4,6,10,11,63,64,74,75,],[9,9,-6,-8,-5,-7,-9,9,9,-4,]),'}':([4,6,10,11,63,74,75,],[-6,-8,-5,-7,-9,75,-4,]),';':([5,16,17,18,19,20,26,27,29,34,35,36,37,38,39,51,52,53,57,60,61,68,69,70,71,72,],[11,-22,-10,-11,-12,-13,-17,-20,-14,54,-32,-34,-35,-36,-37,-15,-16,-27,-21,-18,-19,-31,-33,-28,-29,-30,]),'=':([7,8,73,],[12,14,-26,]),'[':([7,12,],[13,21,]),'(':([9,12,22,23,24,25,32,33,44,45,],[15,23,40,23,42,43,23,23,23,23,]),'INTNUM':([12,13,14,21,40,42,43,46,48,49,50,54,55,],[17,28,29,38,56,58,59,62,65,66,67,38,38,]),'FLONUM':([12,21,54,55,],[18,39,39,39,]),'ONES':([12,],[22,]),'ZEROS':([12,],[24,]),'EYE':([12,],[25,]),'*':([16,26,27,51,52,57,60,61,],[-22,44,-20,44,44,-21,-18,-19,]),'/':([16,26,27,51,52,57,60,61,],[-22,45,-20,45,45,-21,-18,-19,]),'+':([16,20,26,27,41,51,52,57,60,61,],[-22,32,-17,-20,32,-15,-16,-21,-18,-19,]),'-':([16,20,26,27,41,51,52,57,60,61,],[-22,33,-17,-20,33,-15,-16,-21,-18,-19,]),')':([16,26,27,30,41,51,52,56,57,58,59,60,61,65,66,67,],[-22,-17,-20,47,57,-15,-16,70,-21,71,72,-18,-19,-23,-24,-25,]),',':([28,35,36,37,38,39,68,69,],[46,55,-34,-35,-36,-37,55,-33,]),'GREATEREQUAL':([31,],[48,]),'EQUALS':([31,],[49,]),'LOWEREQUAL':([31,],[50,]),']':([34,35,36,37,38,39,62,68,69,],[53,-32,-34,-35,-36,-37,73,-31,-33,]),'{':([47,],[64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instructions_opt':([0,],[2,]),'instructions':([0,64,],[3,74,]),'instruction':([0,3,64,74,],[4,10,4,10,]),'assignment':([0,3,64,74,],[5,5,5,5,]),'if_instruction':([0,3,64,74,],[6,6,6,6,]),'MID':([0,3,64,74,],[8,8,8,8,]),'matrix':([12,],[19,]),'expr':([12,23,],[20,41,]),'term':([12,23,32,33,],[26,26,51,52,]),'factor':([12,23,32,33,44,45,],[27,27,27,27,60,61,]),'relational_expr':([15,],[30,]),'outerlist':([21,],[34,]),'innerlist':([21,54,],[35,68,]),'elem':([21,54,55,],[36,36,69,]),'instructions_block':([47,],[63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instructions_opt','program',1,'p_program','Mparser.py',24),
  ('instructions_opt -> instructions','instructions_opt',1,'p_instructions_opt_1','Mparser.py',27),
  ('instructions_opt -> <empty>','instructions_opt',0,'p_instructions_opt_2','Mparser.py',30),
  ('instructions_block -> { instructions }','instructions_block',3,'p_instructions_block','Mparser.py',33),
  ('instructions -> instructions instruction','instructions',2,'p_instructions_1','Mparser.py',36),
  ('instructions -> instruction','instructions',1,'p_instructions_2','Mparser.py',39),
  ('instruction -> assignment ;','instruction',2,'p_instruction','Mparser.py',42),
  ('instruction -> if_instruction','instruction',1,'p_instruction','Mparser.py',43),
  ('if_instruction -> IF ( relational_expr ) instructions_block','if_instruction',5,'p_if_instruction','Mparser.py',46),
  ('assignment -> ID = INTNUM','assignment',3,'p_assignment','Mparser.py',49),
  ('assignment -> ID = FLONUM','assignment',3,'p_assignment','Mparser.py',50),
  ('assignment -> ID = matrix','assignment',3,'p_assignment','Mparser.py',51),
  ('assignment -> ID = expr','assignment',3,'p_assignment','Mparser.py',52),
  ('assignment -> MID = INTNUM','assignment',3,'p_assignment','Mparser.py',53),
  ('expr -> expr + term','expr',3,'p_expr','Mparser.py',55),
  ('expr -> expr - term','expr',3,'p_expr','Mparser.py',56),
  ('expr -> term','expr',1,'p_expr','Mparser.py',57),
  ('term -> term * factor','term',3,'p_term','Mparser.py',60),
  ('term -> term / factor','term',3,'p_term','Mparser.py',61),
  ('term -> factor','term',1,'p_term','Mparser.py',62),
  ('factor -> ( expr )','factor',3,'p_factor','Mparser.py',65),
  ('factor -> ID','factor',1,'p_factor','Mparser.py',66),
  ('relational_expr -> ID GREATEREQUAL INTNUM','relational_expr',3,'p_relational_expr','Mparser.py',69),
  ('relational_expr -> ID EQUALS INTNUM','relational_expr',3,'p_relational_expr','Mparser.py',70),
  ('relational_expr -> ID LOWEREQUAL INTNUM','relational_expr',3,'p_relational_expr','Mparser.py',71),
  ('MID -> ID [ INTNUM , INTNUM ]','MID',6,'p_MID','Mparser.py',74),
  ('matrix -> [ outerlist ]','matrix',3,'p_matrix','Mparser.py',77),
  ('matrix -> ONES ( INTNUM )','matrix',4,'p_matrix','Mparser.py',78),
  ('matrix -> ZEROS ( INTNUM )','matrix',4,'p_matrix','Mparser.py',79),
  ('matrix -> EYE ( INTNUM )','matrix',4,'p_matrix','Mparser.py',80),
  ('outerlist -> outerlist ; innerlist','outerlist',3,'p_outerlist','Mparser.py',83),
  ('outerlist -> innerlist','outerlist',1,'p_outerlist','Mparser.py',84),
  ('innerlist -> innerlist , elem','innerlist',3,'p_innerlist','Mparser.py',87),
  ('innerlist -> elem','innerlist',1,'p_innerlist','Mparser.py',88),
  ('elem -> ID','elem',1,'p_elem','Mparser.py',91),
  ('elem -> INTNUM','elem',1,'p_elem','Mparser.py',92),
  ('elem -> FLONUM','elem',1,'p_elem','Mparser.py',93),
]
