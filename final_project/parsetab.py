
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA COUT DIV ELSE ENDL EQUALS FOR GREATER IF IGNORE_CONTENT INT LB LBRACKET LESS LPAREN MINUS NUM PLUS PRINT RB RBRACKET RETURN RPAREN SEMICOLON SENTENCE STAR VAR WHILEprogram : statement\n               | program statement\n    statement : INT VAR LPAREN params RPAREN SEMICOLON\n    \n    statement : INT VAR LPAREN params RPAREN\n    \n    params : INT VAR\n           | params COMMA INT VAR\n           |\n    \n    args : VAR\n         | args COMMA VAR\n         | NUM\n         | args COMMA NUM\n         |\n    \n    statement : f_statement\n    \n    f_statement : VAR LPAREN args RPAREN SEMICOLON\n                | VAR EQUALS f_statement\n    \n    statement : INT VAR SEMICOLON\n              | INT VAR EQUALS NUM SEMICOLON\n              | INT VAR EQUALS VAR SEMICOLON\n              | INT VAR EQUALS expr SEMICOLON\n    \n    statement : VAR EQUALS NUM SEMICOLON\n                | array EQUALS NUM SEMICOLON\n                | VAR EQUALS expr SEMICOLON\n                | array EQUALS expr SEMICOLON\n    \n    statement : VAR PLUS PLUS SEMICOLON\n    \n    statement : IF LPAREN condition RPAREN\n    \n    statement : ELSE\n    \n    statement : FOR LPAREN INT VAR EQUALS NUM SEMICOLON condition SEMICOLON for_update RPAREN\n    \n    statement : WHILE LPAREN condition RPAREN\n    \n    condition : VAR GREATER NUM\n                | VAR LESS NUM\n                | VAR GREATER VAR\n                | VAR LESS VAR\n                | VAR EQUALS EQUALS NUM\n    \n    statement : RETURN expr SEMICOLON\n    \n    for_update : VAR PLUS PLUS\n               \n    \n    statement : LB               \n    \n    statement : RB             \n    \n    expr : expr PLUS term\n    expr : expr MINUS termexpr : termterm : term STAR factorterm : term DIV factorterm : factorfactor : LPAREN expr RPARENfactor : NUMfactor : VARfactor : array\n    array : VAR LBRACKET NUM RBRACKET\n    \n    statement : INT STAR VAR SEMICOLON\n    \n    p_content : LESS LESS VAR p_content\n            | LESS LESS SENTENCE p_content\n            | LESS LESS ENDL\n            |\n    \n    statement : COUT p_content SEMICOLON\n\n    '
    
_lr_action_items = {'INT':([0,1,2,5,8,12,13,15,24,35,36,42,54,60,67,69,70,71,75,76,77,82,92,93,94,95,96,98,109,120,],[3,3,-1,-13,-26,-36,-37,-2,52,62,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,110,-18,-17,-19,-14,-3,-27,]),'VAR':([0,1,2,3,5,8,11,12,13,15,17,18,20,22,23,25,29,36,37,42,52,54,55,56,57,58,60,61,62,67,68,69,70,71,73,75,76,77,78,79,82,92,94,95,96,98,109,110,114,116,120,],[4,4,-1,16,-13,-26,31,-36,-37,-2,38,39,44,31,51,51,31,-16,64,-15,81,-34,31,31,31,31,-54,88,91,-49,97,-20,-22,-24,99,-21,-23,-25,101,103,-28,-4,-18,-17,-19,-14,-3,113,51,117,-27,]),'IF':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[7,7,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'ELSE':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[8,8,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'FOR':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[9,9,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'WHILE':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[10,10,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'RETURN':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[11,11,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'LB':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[12,12,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'RB':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[13,13,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'COUT':([0,1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[14,14,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'$end':([1,2,5,8,12,13,15,36,42,54,60,67,69,70,71,75,76,77,82,92,94,95,96,98,109,120,],[0,-1,-13,-26,-36,-37,-2,-16,-15,-34,-54,-49,-20,-22,-24,-21,-23,-25,-28,-4,-18,-17,-19,-14,-3,-27,]),'STAR':([3,27,28,30,31,32,39,40,48,64,65,74,83,84,85,86,87,],[17,57,-43,-45,-46,-47,-46,-45,-45,-46,-45,-48,57,57,-41,-42,-44,]),'EQUALS':([4,6,16,39,51,74,80,81,97,],[18,22,37,68,80,-48,105,106,68,]),'PLUS':([4,19,26,27,28,30,31,32,39,40,41,48,49,59,64,65,66,74,83,84,85,86,87,117,119,],[19,43,55,-40,-43,-45,-46,-47,-46,-45,55,-45,55,55,-46,-45,55,-48,-38,-39,-41,-42,-44,119,121,]),'LPAREN':([4,7,9,10,11,16,18,22,29,37,39,55,56,57,58,97,],[20,23,24,25,29,35,29,29,29,29,20,29,29,29,29,20,]),'LBRACKET':([4,31,39,64,],[21,21,21,21,]),'NUM':([11,18,20,21,22,29,37,55,56,57,58,73,78,79,105,106,],[30,40,46,47,48,30,65,30,30,30,30,100,102,104,111,112,]),'LESS':([14,34,51,88,89,],[34,61,79,34,34,]),'SEMICOLON':([14,16,26,27,28,30,31,32,33,38,39,40,41,43,48,49,64,65,66,72,74,83,84,85,86,87,88,89,90,92,101,102,103,104,107,108,111,112,115,],[-53,36,54,-40,-43,-45,-46,-47,60,67,-46,69,70,71,75,76,94,95,96,98,-48,-38,-39,-41,-42,-44,-53,-53,-52,109,-31,-29,-32,-30,-50,-51,-33,114,116,]),'RPAREN':([20,27,28,30,31,32,35,44,45,46,50,53,59,63,74,83,84,85,86,87,91,99,100,101,102,103,104,111,113,118,121,],[-12,-40,-43,-45,-46,-47,-7,-8,72,-10,77,82,87,92,-48,-38,-39,-41,-42,-44,-5,-9,-11,-31,-29,-32,-30,-33,-6,120,-35,]),'COMMA':([20,35,44,45,46,63,91,99,100,113,],[-12,-7,-8,73,-10,93,-5,-9,-11,-6,]),'MINUS':([26,27,28,30,31,32,39,40,41,48,49,59,64,65,66,74,83,84,85,86,87,],[56,-40,-43,-45,-46,-47,-46,-45,56,-45,56,56,-46,-45,56,-48,-38,-39,-41,-42,-44,]),'DIV':([27,28,30,31,32,39,40,48,64,65,74,83,84,85,86,87,],[58,-43,-45,-46,-47,-46,-45,-45,-46,-45,-48,58,58,-41,-42,-44,]),'RBRACKET':([47,],[74,]),'GREATER':([51,],[78,]),'SENTENCE':([61,],[89,]),'ENDL':([61,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,15,]),'f_statement':([0,1,18,68,],[5,5,42,42,]),'array':([0,1,11,18,22,29,37,55,56,57,58,],[6,6,32,32,32,32,32,32,32,32,32,]),'expr':([11,18,22,29,37,],[26,41,49,59,66,]),'term':([11,18,22,29,37,55,56,],[27,27,27,27,27,83,84,]),'factor':([11,18,22,29,37,55,56,57,58,],[28,28,28,28,28,28,28,85,86,]),'p_content':([14,88,89,],[33,107,108,]),'args':([20,],[45,]),'condition':([23,25,114,],[50,53,115,]),'params':([35,],[63,]),'for_update':([116,],[118,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','skeleton.py',136),
  ('program -> program statement','program',2,'p_program','skeleton.py',137),
  ('statement -> INT VAR LPAREN params RPAREN SEMICOLON','statement',6,'p_func_decl','skeleton.py',146),
  ('statement -> INT VAR LPAREN params RPAREN','statement',5,'p_function','skeleton.py',151),
  ('params -> INT VAR','params',2,'p_func_params','skeleton.py',157),
  ('params -> params COMMA INT VAR','params',4,'p_func_params','skeleton.py',158),
  ('params -> <empty>','params',0,'p_func_params','skeleton.py',159),
  ('args -> VAR','args',1,'p_func_args','skeleton.py',170),
  ('args -> args COMMA VAR','args',3,'p_func_args','skeleton.py',171),
  ('args -> NUM','args',1,'p_func_args','skeleton.py',172),
  ('args -> args COMMA NUM','args',3,'p_func_args','skeleton.py',173),
  ('args -> <empty>','args',0,'p_func_args','skeleton.py',174),
  ('statement -> f_statement','statement',1,'p_f_statement','skeleton.py',185),
  ('f_statement -> VAR LPAREN args RPAREN SEMICOLON','f_statement',5,'p_func_call','skeleton.py',192),
  ('f_statement -> VAR EQUALS f_statement','f_statement',3,'p_func_call','skeleton.py',193),
  ('statement -> INT VAR SEMICOLON','statement',3,'p_statement_decl','skeleton.py',204),
  ('statement -> INT VAR EQUALS NUM SEMICOLON','statement',5,'p_statement_decl','skeleton.py',205),
  ('statement -> INT VAR EQUALS VAR SEMICOLON','statement',5,'p_statement_decl','skeleton.py',206),
  ('statement -> INT VAR EQUALS expr SEMICOLON','statement',5,'p_statement_decl','skeleton.py',207),
  ('statement -> VAR EQUALS NUM SEMICOLON','statement',4,'p_statement_assign','skeleton.py',217),
  ('statement -> array EQUALS NUM SEMICOLON','statement',4,'p_statement_assign','skeleton.py',218),
  ('statement -> VAR EQUALS expr SEMICOLON','statement',4,'p_statement_assign','skeleton.py',219),
  ('statement -> array EQUALS expr SEMICOLON','statement',4,'p_statement_assign','skeleton.py',220),
  ('statement -> VAR PLUS PLUS SEMICOLON','statement',4,'p_statement_plusplus','skeleton.py',226),
  ('statement -> IF LPAREN condition RPAREN','statement',4,'p_statement_if','skeleton.py',233),
  ('statement -> ELSE','statement',1,'p_statement_if_else','skeleton.py',239),
  ('statement -> FOR LPAREN INT VAR EQUALS NUM SEMICOLON condition SEMICOLON for_update RPAREN','statement',11,'p_statement_for','skeleton.py',246),
  ('statement -> WHILE LPAREN condition RPAREN','statement',4,'p_statement_while','skeleton.py',254),
  ('condition -> VAR GREATER NUM','condition',3,'p_condition','skeleton.py',262),
  ('condition -> VAR LESS NUM','condition',3,'p_condition','skeleton.py',263),
  ('condition -> VAR GREATER VAR','condition',3,'p_condition','skeleton.py',264),
  ('condition -> VAR LESS VAR','condition',3,'p_condition','skeleton.py',265),
  ('condition -> VAR EQUALS EQUALS NUM','condition',4,'p_condition','skeleton.py',266),
  ('statement -> RETURN expr SEMICOLON','statement',3,'p_statement_return','skeleton.py',277),
  ('for_update -> VAR PLUS PLUS','for_update',3,'p_for_update','skeleton.py',285),
  ('statement -> LB','statement',1,'p_statement_lb','skeleton.py',292),
  ('statement -> RB','statement',1,'p_statement_rb','skeleton.py',298),
  ('expr -> expr PLUS term','expr',3,'p_expr_plus','skeleton.py',304),
  ('expr -> expr MINUS term','expr',3,'p_expr_minus','skeleton.py',320),
  ('expr -> term','expr',1,'p_expr_term','skeleton.py',328),
  ('term -> term STAR factor','term',3,'p_term_mult','skeleton.py',332),
  ('term -> term DIV factor','term',3,'p_term_div','skeleton.py',336),
  ('term -> factor','term',1,'p_term_factor','skeleton.py',344),
  ('factor -> LPAREN expr RPAREN','factor',3,'p_factor_expr','skeleton.py',349),
  ('factor -> NUM','factor',1,'p_factor_num','skeleton.py',353),
  ('factor -> VAR','factor',1,'p_factor_var','skeleton.py',357),
  ('factor -> array','factor',1,'p_factor_array','skeleton.py',361),
  ('array -> VAR LBRACKET NUM RBRACKET','array',4,'p_array','skeleton.py',366),
  ('statement -> INT STAR VAR SEMICOLON','statement',4,'p_array_decl','skeleton.py',372),
  ('p_content -> LESS LESS VAR p_content','p_content',4,'p_print_content','skeleton.py',378),
  ('p_content -> LESS LESS SENTENCE p_content','p_content',4,'p_print_content','skeleton.py',379),
  ('p_content -> LESS LESS ENDL','p_content',3,'p_print_content','skeleton.py',380),
  ('p_content -> <empty>','p_content',0,'p_print_content','skeleton.py',381),
  ('statement -> COUT p_content SEMICOLON','statement',3,'p_statement_print','skeleton.py',392),
]
