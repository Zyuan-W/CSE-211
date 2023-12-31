
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'COMMA COUT DATA_TYPE DIV ELSE ENDL EQUALS FOR GREATER IF IGNORE_CONTENT INT LB LBRACKET LESS LPAREN MALLOC MINUS NUM PLUS RB RBRACKET RETURN RPAREN SEMICOLON SENTENCE SIZEOF STAR VAR VOID WHILEprogram : statement\n               | program statement\n    statement : IGNORE_CONTENT\n    \n    statement : INT VAR LPAREN params RPAREN SEMICOLON\n                | VOID VAR LPAREN params RPAREN SEMICOLON\n    \n    statement : INT VAR LPAREN params RPAREN\n                | VOID VAR LPAREN params RPAREN\n    \n    params : INT VAR\n           | params COMMA INT VAR\n           | INT STAR VAR\n           | params COMMA INT STAR VAR\n           |\n    \n    args : VAR\n         | args COMMA VAR\n         | NUM\n         | args COMMA NUM\n         |\n    \n    statement : f_statement\n    \n    f_statement : VAR LPAREN args RPAREN SEMICOLON\n                | VAR EQUALS f_statement\n    \n    statement : INT VAR SEMICOLON\n              | INT VAR EQUALS factor SEMICOLON\n              | INT VAR EQUALS expr SEMICOLON\n    \n    statement : VAR EQUALS factor SEMICOLON\n                | VAR EQUALS expr SEMICOLON\n                | array EQUALS factor SEMICOLON\n                | array EQUALS expr SEMICOLON\n    \n    statement : IF LPAREN condition RPAREN\n    \n    statement : ELSE\n    \n    statement : FOR LPAREN INT VAR EQUALS factor SEMICOLON condition SEMICOLON for_update RPAREN\n    \n    statement : WHILE LPAREN condition RPAREN\n    \n    condition : factor GREATER factor\n                | factor LESS factor\n                | factor EQUALS EQUALS factor\n                | factor GREATER EQUALS factor\n                | factor LESS EQUALS factor\n    \n    statement : RETURN expr SEMICOLON\n    \n    statement : factor PLUS EQUALS factor SEMICOLON\n            | factor MINUS EQUALS factor SEMICOLON\n            | factor PLUS PLUS SEMICOLON\n            | factor MINUS MINUS SEMICOLON\n    \n    for_update : VAR PLUS PLUS\n            | VAR MINUS MINUS\n               \n    \n    statement : LB               \n    \n    statement : RB             \n    \n    expr : expr PLUS term\n    expr : expr MINUS termexpr : termterm : term STAR factorterm : term DIV factorterm : factorfactor : NUMfactor : VARfactor : array\n    array : VAR LBRACKET expr RBRACKET\n    \n    statement : INT STAR VAR SEMICOLON\n    \n    statement : VAR EQUALS LPAREN INT STAR RPAREN MALLOC LPAREN SIZEOF LPAREN INT RPAREN STAR factor RPAREN SEMICOLON\n    \n    p_content : LESS LESS VAR p_content\n            | LESS LESS SENTENCE p_content\n            | LESS LESS ENDL\n            |\n    \n    statement : COUT p_content SEMICOLON\n\n    '
    
_lr_action_items = {'IGNORE_CONTENT':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[3,3,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'INT':([0,1,2,3,7,11,15,16,19,30,39,40,46,47,52,63,68,74,76,77,83,85,87,88,89,94,104,105,106,107,110,113,114,115,125,128,142,148,155,],[4,4,-1,-3,-18,-29,-44,-45,-2,61,70,-21,78,-20,70,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,126,-22,-23,-19,-7,-38,-39,-4,-5,145,-30,-57,]),'VOID':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[6,6,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'VAR':([0,1,2,3,4,6,7,11,14,15,16,19,21,22,23,24,28,29,31,40,41,47,54,56,61,63,64,65,66,67,68,69,70,74,75,76,77,80,83,85,87,88,89,90,91,94,103,104,106,107,110,113,114,115,117,119,120,121,125,126,128,134,136,141,148,152,155,],[5,5,-1,-3,20,25,-18,-29,35,-44,-45,-2,42,43,48,35,35,35,35,-21,35,-20,35,35,93,-37,35,35,35,35,-62,99,102,-56,108,-24,-25,111,-40,-41,-26,-27,-28,35,35,-31,124,-6,-22,-23,-19,-7,-38,-39,35,35,35,35,-4,133,-5,137,35,143,-30,35,-57,]),'IF':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[10,10,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'ELSE':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[11,11,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'FOR':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[12,12,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'WHILE':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[13,13,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'RETURN':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[14,14,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'LB':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[15,15,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'RB':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[16,16,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'COUT':([0,1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[17,17,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'NUM':([0,1,2,3,7,11,14,15,16,19,22,23,24,28,29,31,40,41,47,54,56,63,64,65,66,67,68,74,76,77,80,83,85,87,88,89,90,91,94,104,106,107,110,113,114,115,117,119,120,121,125,128,136,148,152,155,],[18,18,-1,-3,-18,-29,18,-44,-45,-2,18,50,18,18,18,18,-21,18,-20,18,18,-37,18,18,18,18,-62,-56,-24,-25,112,-40,-41,-26,-27,-28,18,18,-31,-6,-22,-23,-19,-7,-38,-39,18,18,18,18,-4,-5,18,-30,18,-57,]),'$end':([1,2,3,7,11,15,16,19,40,47,63,68,74,76,77,83,85,87,88,89,94,104,106,107,110,113,114,115,125,128,148,155,],[0,-1,-3,-18,-29,-44,-45,-2,-21,-20,-37,-62,-56,-24,-25,-40,-41,-26,-27,-28,-31,-6,-22,-23,-19,-7,-38,-39,-4,-5,-30,-57,]),'STAR':([4,18,33,34,35,36,43,44,57,70,72,78,81,95,96,97,98,126,149,],[21,-52,66,-51,-53,-54,-53,-51,-51,103,-51,109,-55,66,66,-49,-50,134,152,]),'EQUALS':([5,9,18,20,26,27,35,36,43,60,81,90,91,92,93,108,],[22,28,-52,41,54,56,-53,-54,75,92,-55,117,119,120,121,75,]),'LPAREN':([5,10,12,13,20,22,25,43,108,135,140,],[23,29,30,31,39,46,52,23,23,138,142,]),'LBRACKET':([5,35,43,],[24,24,24,]),'PLUS':([5,8,9,18,26,32,33,34,35,36,43,44,45,51,57,58,72,73,81,95,96,97,98,143,146,],[-53,26,-54,-52,53,64,-48,-51,-53,-54,-53,-51,64,64,-51,64,-51,64,-55,-46,-47,-49,-50,146,150,]),'MINUS':([5,8,9,18,27,32,33,34,35,36,43,44,45,51,57,58,72,73,81,95,96,97,98,143,147,],[-53,27,-54,-52,55,65,-48,-51,-53,-54,-53,-51,65,65,-51,65,-51,65,-55,-46,-47,-49,-50,147,151,]),'LESS':([17,18,35,36,38,60,81,99,100,],[38,-52,-53,-54,69,91,-55,38,38,]),'SEMICOLON':([17,18,20,32,33,34,35,36,37,42,43,44,45,53,55,57,58,72,73,79,81,84,86,95,96,97,98,99,100,101,104,113,116,118,122,123,129,130,131,132,139,154,],[-61,-52,40,63,-48,-51,-53,-54,68,74,-53,76,77,83,85,87,88,106,107,110,-55,114,115,-46,-47,-49,-50,-61,-61,-60,125,128,-32,-33,-58,-59,-35,-36,-34,136,141,155,]),'DIV':([18,33,34,35,36,43,44,57,72,81,95,96,97,98,],[-52,67,-51,-53,-54,-53,-51,-51,-51,-55,67,67,-49,-50,]),'RBRACKET':([18,33,34,35,36,51,81,95,96,97,98,],[-52,-48,-51,-53,-54,81,-55,-46,-47,-49,-50,]),'GREATER':([18,35,36,60,81,],[-52,-53,-54,90,-55,]),'RPAREN':([18,23,35,36,39,48,49,50,52,59,62,71,81,82,102,109,111,112,116,118,124,129,130,131,133,137,144,145,150,151,153,],[-52,-17,-53,-54,-12,-13,79,-15,-12,89,94,104,-55,113,-8,127,-14,-16,-32,-33,-10,-35,-36,-34,-9,-11,148,149,-42,-43,154,]),'COMMA':([23,39,48,49,50,52,71,82,102,111,112,124,133,137,],[-17,-12,-13,80,-15,-12,105,105,-8,-14,-16,-10,-9,-11,]),'SENTENCE':([69,],[100,]),'ENDL':([69,],[101,]),'MALLOC':([127,],[135,]),'SIZEOF':([138,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement':([0,1,],[2,19,]),'f_statement':([0,1,22,75,],[7,7,47,47,]),'factor':([0,1,14,22,24,28,29,31,41,54,56,64,65,66,67,90,91,117,119,120,121,136,152,],[8,8,34,44,34,57,60,60,72,84,86,34,34,97,98,116,118,129,130,131,132,60,153,]),'array':([0,1,14,22,24,28,29,31,41,54,56,64,65,66,67,90,91,117,119,120,121,136,152,],[9,9,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'expr':([14,22,24,28,41,],[32,45,51,58,73,]),'term':([14,22,24,28,41,64,65,],[33,33,33,33,33,95,96,]),'p_content':([17,99,100,],[37,122,123,]),'args':([23,],[49,]),'condition':([29,31,136,],[59,62,139,]),'params':([39,52,],[71,82,]),'for_update':([141,],[144,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','skeleton.py',185),
  ('program -> program statement','program',2,'p_program','skeleton.py',186),
  ('statement -> IGNORE_CONTENT','statement',1,'p_statement_IGNORE_CONTENT','skeleton.py',194),
  ('statement -> INT VAR LPAREN params RPAREN SEMICOLON','statement',6,'p_func_decl','skeleton.py',202),
  ('statement -> VOID VAR LPAREN params RPAREN SEMICOLON','statement',6,'p_func_decl','skeleton.py',203),
  ('statement -> INT VAR LPAREN params RPAREN','statement',5,'p_function','skeleton.py',212),
  ('statement -> VOID VAR LPAREN params RPAREN','statement',5,'p_function','skeleton.py',213),
  ('params -> INT VAR','params',2,'p_func_params','skeleton.py',220),
  ('params -> params COMMA INT VAR','params',4,'p_func_params','skeleton.py',221),
  ('params -> INT STAR VAR','params',3,'p_func_params','skeleton.py',222),
  ('params -> params COMMA INT STAR VAR','params',5,'p_func_params','skeleton.py',223),
  ('params -> <empty>','params',0,'p_func_params','skeleton.py',224),
  ('args -> VAR','args',1,'p_func_args','skeleton.py',239),
  ('args -> args COMMA VAR','args',3,'p_func_args','skeleton.py',240),
  ('args -> NUM','args',1,'p_func_args','skeleton.py',241),
  ('args -> args COMMA NUM','args',3,'p_func_args','skeleton.py',242),
  ('args -> <empty>','args',0,'p_func_args','skeleton.py',243),
  ('statement -> f_statement','statement',1,'p_f_statement','skeleton.py',254),
  ('f_statement -> VAR LPAREN args RPAREN SEMICOLON','f_statement',5,'p_func_call','skeleton.py',262),
  ('f_statement -> VAR EQUALS f_statement','f_statement',3,'p_func_call','skeleton.py',263),
  ('statement -> INT VAR SEMICOLON','statement',3,'p_statement_decl','skeleton.py',276),
  ('statement -> INT VAR EQUALS factor SEMICOLON','statement',5,'p_statement_decl','skeleton.py',277),
  ('statement -> INT VAR EQUALS expr SEMICOLON','statement',5,'p_statement_decl','skeleton.py',278),
  ('statement -> VAR EQUALS factor SEMICOLON','statement',4,'p_statement_assign','skeleton.py',303),
  ('statement -> VAR EQUALS expr SEMICOLON','statement',4,'p_statement_assign','skeleton.py',304),
  ('statement -> array EQUALS factor SEMICOLON','statement',4,'p_statement_assign','skeleton.py',305),
  ('statement -> array EQUALS expr SEMICOLON','statement',4,'p_statement_assign','skeleton.py',306),
  ('statement -> IF LPAREN condition RPAREN','statement',4,'p_statement_if','skeleton.py',323),
  ('statement -> ELSE','statement',1,'p_statement_if_else','skeleton.py',331),
  ('statement -> FOR LPAREN INT VAR EQUALS factor SEMICOLON condition SEMICOLON for_update RPAREN','statement',11,'p_statement_for','skeleton.py',339),
  ('statement -> WHILE LPAREN condition RPAREN','statement',4,'p_statement_while','skeleton.py',348),
  ('condition -> factor GREATER factor','condition',3,'p_condition','skeleton.py',356),
  ('condition -> factor LESS factor','condition',3,'p_condition','skeleton.py',357),
  ('condition -> factor EQUALS EQUALS factor','condition',4,'p_condition','skeleton.py',358),
  ('condition -> factor GREATER EQUALS factor','condition',4,'p_condition','skeleton.py',359),
  ('condition -> factor LESS EQUALS factor','condition',4,'p_condition','skeleton.py',360),
  ('statement -> RETURN expr SEMICOLON','statement',3,'p_statement_return','skeleton.py',371),
  ('statement -> factor PLUS EQUALS factor SEMICOLON','statement',5,'p_statement_update','skeleton.py',383),
  ('statement -> factor MINUS EQUALS factor SEMICOLON','statement',5,'p_statement_update','skeleton.py',384),
  ('statement -> factor PLUS PLUS SEMICOLON','statement',4,'p_statement_update','skeleton.py',385),
  ('statement -> factor MINUS MINUS SEMICOLON','statement',4,'p_statement_update','skeleton.py',386),
  ('for_update -> VAR PLUS PLUS','for_update',3,'p_for_update','skeleton.py',400),
  ('for_update -> VAR MINUS MINUS','for_update',3,'p_for_update','skeleton.py',401),
  ('statement -> LB','statement',1,'p_statement_lb','skeleton.py',411),
  ('statement -> RB','statement',1,'p_statement_rb','skeleton.py',418),
  ('expr -> expr PLUS term','expr',3,'p_expr_plus','skeleton.py',425),
  ('expr -> expr MINUS term','expr',3,'p_expr_minus','skeleton.py',441),
  ('expr -> term','expr',1,'p_expr_term','skeleton.py',453),
  ('term -> term STAR factor','term',3,'p_term_mult','skeleton.py',457),
  ('term -> term DIV factor','term',3,'p_term_div','skeleton.py',461),
  ('term -> factor','term',1,'p_term_factor','skeleton.py',469),
  ('factor -> NUM','factor',1,'p_factor_num','skeleton.py',483),
  ('factor -> VAR','factor',1,'p_factor_var','skeleton.py',487),
  ('factor -> array','factor',1,'p_factor_array','skeleton.py',491),
  ('array -> VAR LBRACKET expr RBRACKET','array',4,'p_array','skeleton.py',497),
  ('statement -> INT STAR VAR SEMICOLON','statement',4,'p_array_decl','skeleton.py',507),
  ('statement -> VAR EQUALS LPAREN INT STAR RPAREN MALLOC LPAREN SIZEOF LPAREN INT RPAREN STAR factor RPAREN SEMICOLON','statement',16,'p_array_init','skeleton.py',515),
  ('p_content -> LESS LESS VAR p_content','p_content',4,'p_print_content','skeleton.py',522),
  ('p_content -> LESS LESS SENTENCE p_content','p_content',4,'p_print_content','skeleton.py',523),
  ('p_content -> LESS LESS ENDL','p_content',3,'p_print_content','skeleton.py',524),
  ('p_content -> <empty>','p_content',0,'p_print_content','skeleton.py',525),
  ('statement -> COUT p_content SEMICOLON','statement',3,'p_statement_print','skeleton.py',537),
]
