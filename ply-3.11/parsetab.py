
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND CHAR COMILLA COMMA COMPARE CTEC CTEF CTEI CTESTRING DIV DO ELSE END EQUALS FLOAT FOR FROM FUNCTION GT GTE ID IF INT LBRACKET LCURLY LPAREN LT LTE MEDIA MINUS MODA MUL NE OR PLOTXY PLUS PRINCIPAL PROGRAM RBRACKET RCURLY READ RETURN RPAREN SEMMICOLON SIMPLEREGRESSION THEN TO TWOPOINTS VARIANZA VARS VOID WHILE WRITE\n    program : PROGRAM ID SEMMICOLON addProgram program1 \n    \n    addProgram :\n    \n    program1 : vars functions program2\n            | vars functions \n            | program2\n    \n    program2 : principal\n    \n    principal : PRINCIPAL saveFunction LPAREN RPAREN LCURLY vars statements RCURLY \n    \n    statements : assign SEMMICOLON statements \n        | functionCall SEMMICOLON statements \n        | read statements SEMMICOLON statements\n        | write statements SEMMICOLON statements \n        | for statements \n        | while statements \n        | if statements \n        | return statements\n        | empty\n    \n    assign : ID add_id2 EQUALS saveOperator exp generateAssignQuad\n            | ID add_id2 arr EQUALS saveOperator exp generateAssignQuad\n    generateAssignQuad :  add_id :  add_id2 : \n    functionCall : ID LPAREN exp RPAREN\n    \n    media : MEDIA LPAREN arr RPAREN SEMMICOLON\n    \n    read : READ operatorRead LPAREN paramRead RPAREN \n    \n    paramRead : paramReadAux \n              | empty \n    \n    paramReadAux : exp generateQuadREAD \n                 | exp generateQuadREAD COMMA operatorRead paramReadAux \n    \n    operatorRead : \n    \n    generateQuadREAD : \n    \n    write : WRITE writeOperator LPAREN paramWrite RPAREN\n    \n    paramWrite : paramWriteAux \n               | empty \n    \n    paramWriteAux : exp generateQuadPRINT \n                  | exp generateQuadPRINT COMMA writeOperator paramWriteAux \n    \n    writeOperator : \n    \n    generateQuadPRINT :\n    \n    LoopEnd :\n    \n    for : FOR forOP assign TO CTEI DO generateQuadFOR LCURLY statements RCURLY LoopEnd\n    \n    forOP :\n    \n    generateQuadFOR :\n    \n    while : WHILE whileOP LPAREN exp RPAREN DO generateQuadWHILE LCURLY statements RCURLY LoopEnd\n    \n    whileOP : \n    \n    generateQuadWHILE :\n    \n    if : IF LPAREN exp RPAREN generateQuadIF THEN LCURLY statements RCURLY else endIF\n    \n    else : ELSE generateQuadELSE LCURLY statements RCURLY\n            | empty \n    \n    generateQuadIF : \n    \n    endIF : \n    \n    generateQuadELSE :\n    \n    exp : nexp generateQuadOR\n        | nexp generateQuadOR OR saveOperator nexp \n    \n    generateQuadOR : \n    \n    nexp : compexp generateQuadAND\n        | compexp generateQuadAND AND saveOperator compexp \n    \n    generateQuadAND : \n    \n    compexp : sumexp \n            | compexp1 sumexp \n    \n    compexp1 : sumexp GT saveOperator sumexp generateQuadCOMPARE\n             | sumexp LT saveOperator sumexp generateQuadCOMPARE\n             | sumexp GTE saveOperator sumexp generateQuadCOMPARE\n             | sumexp LTE saveOperator sumexp generateQuadCOMPARE\n             | sumexp NE saveOperator sumexp generateQuadCOMPARE\n    \n    generateQuadCOMPARE : \n    \n    sumexp : mulexp \n           | mulexp PLUS saveOperator mulexp generateQuadSUM \n           | mulexp MINUS saveOperator mulexp generateQuadSUM\n    \n    generateQuadSUM :\n    \n    mulexp : pexp \n           | pexp MUL saveOperator pexp generateQuadMUL\n           | pexp DIV saveOperator pexp generateQuadMUL\n    \n    generateQuadMUL : \n    \n    pexp : ID add_id2\n         | CTEI saveCTE\n         | CTEF saveCTE\n         | CTEC saveCTE\n         | CTESTRING saveCTE\n         | functionCall \n         | LPAREN exp RPAREN \n     saveCTE :  saveOperator : \n    vars : var\n        | empty\n    \n    var : VARS var2 \n    \n    var2 : var2 type TWOPOINTS var1 SEMMICOLON addVar\n         | empty \n    \n    var1 : ID \n         | ID COMMA var1 addVar\n         | ID arr \n         | ID arr COMMA var1 addVar\n         | empty \n    addVar :\n    saveTypeVar : \n    \n    type : INT saveTypeVar\n         | CHAR saveTypeVar\n         | FLOAT saveTypeVar \n    \n    arr : LBRACKET CTEI RBRACKET \n        | LBRACKET exp RBRACKET\n    \n    functions : FUNCTION INT functions1 functions\n              | FUNCTION CHAR functions1 functions\n              | FUNCTION FLOAT functions1 functions\n              | FUNCTION VOID functions1 functions\n              | empty\n    \n    functions1 : ID saveFunction LPAREN args RPAREN vars LCURLY statements RCURLY  \n               | empty\n    \n    saveFunction : \n    \n    args : args type TWOPOINTS var1 addVar\n         | empty \n    \n    args1 : ID addVar\n          | ID COMMA args1 \n          | empty \n    \n    return : RETURN LPAREN exp RPAREN SEMMICOLON\n            | RETURN LPAREN exp RPAREN \n    \n    empty :  \n    '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,4,5,6,7,8,9,10,11,12,14,16,17,18,20,21,22,23,24,30,32,33,34,35,41,43,44,45,51,58,118,216,],[0,-2,-114,-1,-114,-5,-82,-83,-6,-114,-4,-103,-84,-86,-3,-114,-114,-114,-114,-114,-105,-114,-114,-114,-99,-100,-101,-102,-92,-85,-7,-104,]),'ID':([2,9,10,12,17,18,21,22,23,24,36,49,51,52,54,55,58,60,66,67,68,69,70,71,72,73,74,78,79,80,81,82,83,88,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,119,120,130,132,133,135,137,138,139,140,141,142,143,144,145,146,147,149,152,153,154,156,157,160,163,165,166,167,168,169,170,171,172,173,174,175,176,179,180,192,197,198,199,200,201,202,203,204,205,207,208,210,215,219,220,225,226,229,232,233,237,238,239,240,242,243,244,245,247,249,],[3,-82,-83,-114,-84,-86,31,31,31,31,47,-114,-92,47,69,85,-85,47,69,-65,-69,-21,-80,-80,-80,-78,69,85,85,85,85,85,85,-40,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,69,-75,-76,-77,85,85,159,69,69,47,-81,-81,69,69,69,69,69,69,69,69,69,-79,85,85,-81,69,69,69,85,69,69,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,69,-81,-113,-59,-60,-61,-62,-63,-66,-67,-70,-71,69,-24,-31,-112,-29,-36,69,69,85,85,85,-114,-38,-38,-49,-47,-39,-42,-45,85,-46,]),'SEMMICOLON':([3,36,46,47,48,52,53,59,60,63,64,65,67,68,69,70,71,72,73,76,77,78,79,80,81,82,83,84,94,95,96,97,98,99,100,106,107,112,114,115,116,119,120,121,122,123,124,125,126,136,149,150,151,152,153,172,173,174,175,176,177,178,192,195,196,202,203,204,205,206,208,210,215,217,218,224,237,238,239,240,242,243,244,245,249,],[4,-114,51,-87,-91,-114,-89,-92,-114,-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,119,120,-114,-114,-114,-114,-114,-114,-16,-88,-92,-97,-74,-98,-51,-54,-58,-80,-73,-75,-76,-77,-114,-114,152,153,-12,-13,-14,-15,-90,-79,-8,-9,-114,-114,-68,-68,-72,-72,-22,-10,-11,215,-52,-55,-66,-67,-70,-71,-19,-24,-31,-112,-17,-19,-18,-114,-38,-38,-49,-47,-39,-42,-45,-46,]),'VARS':([4,5,49,92,],[-2,12,12,12,]),'PRINCIPAL':([4,5,7,9,10,12,14,16,17,18,21,22,23,24,30,32,33,34,35,41,43,44,45,51,58,216,],[-2,13,-114,-82,-83,-114,13,-103,-84,-86,-114,-114,-114,-114,-114,-105,-114,-114,-114,-99,-100,-101,-102,-92,-85,-104,]),'FUNCTION':([4,5,7,9,10,12,17,18,21,22,23,24,30,32,33,34,35,51,58,216,],[-2,-114,15,-82,-83,-114,-84,-86,-114,-114,-114,-114,15,-105,15,15,15,-92,-85,-104,]),'READ':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,86,-85,86,86,86,86,86,86,86,86,86,86,86,-113,-24,-31,-112,86,86,86,-114,-38,-38,-49,-47,-39,-42,-45,86,-46,]),'WRITE':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,87,-85,87,87,87,87,87,87,87,87,87,87,87,-113,-24,-31,-112,87,87,87,-114,-38,-38,-49,-47,-39,-42,-45,87,-46,]),'FOR':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,88,-85,88,88,88,88,88,88,88,88,88,88,88,-113,-24,-31,-112,88,88,88,-114,-38,-38,-49,-47,-39,-42,-45,88,-46,]),'WHILE':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,89,-85,89,89,89,89,89,89,89,89,89,89,89,-113,-24,-31,-112,89,89,89,-114,-38,-38,-49,-47,-39,-42,-45,89,-46,]),'IF':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,90,-85,90,90,90,90,90,90,90,90,90,90,90,-113,-24,-31,-112,90,90,90,-114,-38,-38,-49,-47,-39,-42,-45,90,-46,]),'RETURN':([9,10,12,17,18,49,51,55,58,78,79,80,81,82,83,119,120,152,153,163,192,208,210,215,229,232,233,237,238,239,240,242,243,244,245,247,249,],[-82,-83,-114,-84,-86,-114,-92,91,-85,91,91,91,91,91,91,91,91,91,91,91,-113,-24,-31,-112,91,91,91,-114,-38,-38,-49,-47,-39,-42,-45,91,-46,]),'RCURLY':([9,10,12,17,18,49,51,55,58,75,80,81,82,83,84,119,120,123,124,125,126,150,151,152,153,163,177,178,192,193,215,229,232,233,234,235,236,237,238,239,240,242,243,244,245,247,248,249,],[-82,-83,-114,-84,-86,-114,-92,-114,-85,118,-114,-114,-114,-114,-16,-114,-114,-12,-13,-14,-15,-8,-9,-114,-114,-114,-10,-11,-113,216,-112,-114,-114,-114,237,238,239,-114,-38,-38,-49,-47,-39,-42,-45,-114,249,-46,]),'LCURLY':([9,10,12,17,18,40,51,58,92,134,221,222,223,227,228,241,246,],[-82,-83,-114,-84,-86,49,-92,-85,-114,163,-41,-44,229,232,233,-50,247,]),'INT':([12,15,17,18,47,48,50,51,52,53,56,57,58,59,60,94,95,96,98,135,136,164,194,],[-114,21,26,-86,-87,-91,-114,-92,-114,-89,26,-108,-85,-92,-114,-88,-92,-97,-98,-114,-90,-92,-107,]),'CHAR':([12,15,17,18,47,48,50,51,52,53,56,57,58,59,60,94,95,96,98,135,136,164,194,],[-114,22,27,-86,-87,-91,-114,-92,-114,-89,27,-108,-85,-92,-114,-88,-92,-97,-98,-114,-90,-92,-107,]),'FLOAT':([12,15,17,18,47,48,50,51,52,53,56,57,58,59,60,94,95,96,98,135,136,164,194,],[-114,23,28,-86,-87,-91,-114,-92,-114,-89,28,-108,-85,-92,-114,-88,-92,-97,-98,-114,-90,-92,-107,]),'LPAREN':([13,19,31,42,54,66,67,68,69,70,71,72,73,74,85,86,87,89,90,91,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,128,129,131,132,133,137,138,139,140,141,142,143,144,145,146,147,149,154,156,157,160,165,166,167,168,169,170,171,172,173,174,175,176,179,180,197,198,199,200,201,202,203,204,205,207,219,220,225,226,],[-106,29,-106,50,74,74,-65,-69,113,-80,-80,-80,-78,74,113,-29,-36,-43,132,133,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,74,-75,-76,-77,156,157,160,74,74,-81,-81,74,74,74,74,74,74,74,74,74,-79,-81,74,74,74,74,74,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,74,-81,-59,-60,-61,-62,-63,-66,-67,-70,-71,74,-29,-36,74,74,]),'VOID':([15,],[24,]),'TWOPOINTS':([25,26,27,28,37,38,39,93,],[36,-93,-93,-93,-94,-95,-96,135,]),'RPAREN':([29,47,48,50,52,53,56,57,59,60,63,64,65,67,68,69,70,71,72,73,94,95,96,97,98,99,100,106,107,112,114,115,116,117,135,136,148,149,156,157,161,162,164,172,173,174,175,176,181,182,183,184,185,186,187,188,190,194,195,196,202,203,204,205,209,211,230,231,],[40,-87,-91,-114,-114,-89,92,-108,-92,-114,-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,-88,-92,-97,-74,-98,-51,-54,-58,-80,-73,-75,-76,-77,149,-114,-90,176,-79,-114,-114,191,192,-92,-68,-68,-72,-72,-22,208,-25,-26,-30,210,-32,-33,-37,213,-107,-52,-55,-66,-67,-70,-71,-27,-34,-28,-35,]),'COMMA':([47,53,63,64,65,67,68,69,70,71,72,73,96,97,98,99,100,106,107,112,114,115,116,149,172,173,174,175,176,184,188,195,196,202,203,204,205,209,211,],[52,60,-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,-97,-74,-98,-51,-54,-58,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-30,-37,-52,-55,-66,-67,-70,-71,219,220,]),'LBRACKET':([47,85,127,159,],[54,-21,54,-21,]),'CTEI':([54,66,67,68,69,70,71,72,73,74,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,132,133,137,138,139,140,141,142,143,144,145,146,147,149,154,156,157,160,165,166,167,168,169,170,171,172,173,174,175,176,179,180,189,197,198,199,200,201,202,203,204,205,207,219,220,225,226,],[61,107,-65,-69,-21,-80,-80,-80,-78,107,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,107,-75,-76,-77,107,107,-81,-81,107,107,107,107,107,107,107,107,107,-79,-81,107,107,107,107,107,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,107,-81,212,-59,-60,-61,-62,-63,-66,-67,-70,-71,107,-29,-36,107,107,]),'CTEF':([54,66,67,68,69,70,71,72,73,74,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,132,133,137,138,139,140,141,142,143,144,145,146,147,149,154,156,157,160,165,166,167,168,169,170,171,172,173,174,175,176,179,180,197,198,199,200,201,202,203,204,205,207,219,220,225,226,],[70,70,-65,-69,-21,-80,-80,-80,-78,70,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,70,-75,-76,-77,70,70,-81,-81,70,70,70,70,70,70,70,70,70,-79,-81,70,70,70,70,70,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,70,-81,-59,-60,-61,-62,-63,-66,-67,-70,-71,70,-29,-36,70,70,]),'CTEC':([54,66,67,68,69,70,71,72,73,74,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,132,133,137,138,139,140,141,142,143,144,145,146,147,149,154,156,157,160,165,166,167,168,169,170,171,172,173,174,175,176,179,180,197,198,199,200,201,202,203,204,205,207,219,220,225,226,],[71,71,-65,-69,-21,-80,-80,-80,-78,71,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,71,-75,-76,-77,71,71,-81,-81,71,71,71,71,71,71,71,71,71,-79,-81,71,71,71,71,71,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,71,-81,-59,-60,-61,-62,-63,-66,-67,-70,-71,71,-29,-36,71,71,]),'CTESTRING':([54,66,67,68,69,70,71,72,73,74,97,101,102,103,104,105,107,108,109,110,111,112,113,114,115,116,132,133,137,138,139,140,141,142,143,144,145,146,147,149,154,156,157,160,165,166,167,168,169,170,171,172,173,174,175,176,179,180,197,198,199,200,201,202,203,204,205,207,219,220,225,226,],[72,72,-65,-69,-21,-80,-80,-80,-78,72,-74,-81,-81,-81,-81,-81,-80,-81,-81,-81,-81,-73,72,-75,-76,-77,72,72,-81,-81,72,72,72,72,72,72,72,72,72,-79,-81,72,72,72,72,72,-64,-64,-64,-64,-64,-68,-68,-72,-72,-22,72,-81,-59,-60,-61,-62,-63,-66,-67,-70,-71,72,-29,-36,72,72,]),'RBRACKET':([61,62,63,64,65,67,68,69,70,71,72,73,97,99,100,106,107,112,114,115,116,149,172,173,174,175,176,195,196,202,203,204,205,],[96,98,-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,-74,-51,-54,-58,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-52,-55,-66,-67,-70,-71,]),'MUL':([61,68,69,70,71,72,73,97,107,112,114,115,116,149,176,],[-80,110,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-22,]),'DIV':([61,68,69,70,71,72,73,97,107,112,114,115,116,149,176,],[-80,111,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-22,]),'PLUS':([61,67,68,69,70,71,72,73,97,107,112,114,115,116,149,174,175,176,204,205,],[-80,108,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-72,-72,-22,-70,-71,]),'MINUS':([61,67,68,69,70,71,72,73,97,107,112,114,115,116,149,174,175,176,204,205,],[-80,109,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-72,-72,-22,-70,-71,]),'GT':([61,65,67,68,69,70,71,72,73,97,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,101,-65,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'LT':([61,65,67,68,69,70,71,72,73,97,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,102,-65,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'GTE':([61,65,67,68,69,70,71,72,73,97,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,103,-65,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'LTE':([61,65,67,68,69,70,71,72,73,97,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,104,-65,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'NE':([61,65,67,68,69,70,71,72,73,97,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,105,-65,-69,-21,-80,-80,-80,-78,-74,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'AND':([61,64,65,67,68,69,70,71,72,73,97,100,106,107,112,114,115,116,149,172,173,174,175,176,202,203,204,205,],[-80,-56,-57,-65,-69,-21,-80,-80,-80,-78,-74,138,-58,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-66,-67,-70,-71,]),'OR':([61,63,64,65,67,68,69,70,71,72,73,97,99,100,106,107,112,114,115,116,149,172,173,174,175,176,196,202,203,204,205,],[-80,-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,-74,137,-54,-58,-80,-73,-75,-76,-77,-79,-68,-68,-72,-72,-22,-55,-66,-67,-70,-71,]),'TO':([63,64,65,67,68,69,70,71,72,73,97,99,100,106,107,112,114,115,116,149,158,172,173,174,175,176,195,196,202,203,204,205,206,217,218,224,],[-53,-56,-57,-65,-69,-21,-80,-80,-80,-78,-74,-51,-54,-58,-80,-73,-75,-76,-77,-79,189,-68,-68,-72,-72,-22,-52,-55,-66,-67,-70,-71,-19,-17,-19,-18,]),'EQUALS':([85,96,98,127,155,159,],[-21,-97,-98,154,180,-21,]),'THEN':([191,214,],[-48,223,]),'DO':([212,213,],[221,222,]),'ELSE':([237,],[241,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'addProgram':([4,],[5,]),'program1':([5,],[6,]),'vars':([5,49,92,],[7,55,134,]),'program2':([5,14,],[8,20,]),'var':([5,49,92,],[9,9,9,]),'empty':([5,7,12,21,22,23,24,30,33,34,35,36,49,50,52,55,60,78,79,80,81,82,83,92,119,120,135,152,153,156,157,163,229,232,233,237,247,],[10,16,18,32,32,32,32,16,16,16,16,48,10,57,48,84,48,84,84,84,84,84,84,10,84,84,48,84,84,183,187,84,84,84,84,242,84,]),'principal':([5,14,],[11,11,]),'functions':([7,30,33,34,35,],[14,41,43,44,45,]),'var2':([12,],[17,]),'saveFunction':([13,31,],[19,42,]),'type':([17,56,],[25,93,]),'functions1':([21,22,23,24,],[30,33,34,35,]),'saveTypeVar':([26,27,28,],[37,38,39,]),'var1':([36,52,60,135,],[46,59,95,164,]),'arr':([47,127,],[53,155,]),'args':([50,],[56,]),'addVar':([51,59,95,164,],[58,94,136,194,]),'exp':([54,74,113,132,133,156,157,160,179,207,225,226,],[62,117,148,161,162,184,188,190,206,218,184,188,]),'nexp':([54,74,113,132,133,156,157,160,165,179,207,225,226,],[63,63,63,63,63,63,63,63,195,63,63,63,63,]),'compexp':([54,74,113,132,133,156,157,160,165,166,179,207,225,226,],[64,64,64,64,64,64,64,64,64,196,64,64,64,64,]),'sumexp':([54,66,74,113,132,133,139,140,141,142,143,156,157,160,165,166,179,207,225,226,],[65,106,65,65,65,65,167,168,169,170,171,65,65,65,65,65,65,65,65,65,]),'compexp1':([54,74,113,132,133,156,157,160,165,166,179,207,225,226,],[66,66,66,66,66,66,66,66,66,66,66,66,66,66,]),'mulexp':([54,66,74,113,132,133,139,140,141,142,143,144,145,156,157,160,165,166,179,207,225,226,],[67,67,67,67,67,67,67,67,67,67,67,172,173,67,67,67,67,67,67,67,67,67,]),'pexp':([54,66,74,113,132,133,139,140,141,142,143,144,145,146,147,156,157,160,165,166,179,207,225,226,],[68,68,68,68,68,68,68,68,68,68,68,68,68,174,175,68,68,68,68,68,68,68,68,68,]),'functionCall':([54,55,66,74,78,79,80,81,82,83,113,119,120,132,133,139,140,141,142,143,144,145,146,147,152,153,156,157,160,163,165,166,179,207,225,226,229,232,233,247,],[73,77,73,73,77,77,77,77,77,77,73,77,77,73,73,73,73,73,73,73,73,73,73,73,77,77,73,73,73,77,73,73,73,73,73,73,77,77,77,77,]),'statements':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[75,121,122,123,124,125,126,150,151,177,178,193,234,235,236,248,]),'assign':([55,78,79,80,81,82,83,119,120,130,152,153,163,229,232,233,247,],[76,76,76,76,76,76,76,76,76,158,76,76,76,76,76,76,76,]),'read':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'write':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'for':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'while':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'if':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'return':([55,78,79,80,81,82,83,119,120,152,153,163,229,232,233,247,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'saveCTE':([61,70,71,72,107,],[97,114,115,116,97,]),'generateQuadOR':([63,],[99,]),'generateQuadAND':([64,],[100,]),'add_id2':([69,85,159,],[112,127,127,]),'operatorRead':([86,219,],[128,225,]),'writeOperator':([87,220,],[129,226,]),'forOP':([88,],[130,]),'whileOP':([89,],[131,]),'saveOperator':([101,102,103,104,105,108,109,110,111,137,138,154,180,],[139,140,141,142,143,144,145,146,147,165,166,179,207,]),'paramRead':([156,],[181,]),'paramReadAux':([156,225,],[182,230,]),'paramWrite':([157,],[185,]),'paramWriteAux':([157,226,],[186,231,]),'generateQuadCOMPARE':([167,168,169,170,171,],[197,198,199,200,201,]),'generateQuadSUM':([172,173,],[202,203,]),'generateQuadMUL':([174,175,],[204,205,]),'generateQuadREAD':([184,],[209,]),'generateQuadPRINT':([188,],[211,]),'generateQuadIF':([191,],[214,]),'generateAssignQuad':([206,218,],[217,224,]),'generateQuadFOR':([221,],[227,]),'generateQuadWHILE':([222,],[228,]),'else':([237,],[240,]),'LoopEnd':([238,239,],[243,244,]),'endIF':([240,],[245,]),'generateQuadELSE':([241,],[246,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID SEMMICOLON addProgram program1','program',5,'p_program','main.py',161),
  ('addProgram -> <empty>','addProgram',0,'p_addProgram','main.py',167),
  ('program1 -> vars functions program2','program1',3,'p_program1','main.py',187),
  ('program1 -> vars functions','program1',2,'p_program1','main.py',188),
  ('program1 -> program2','program1',1,'p_program1','main.py',189),
  ('program2 -> principal','program2',1,'p_program2','main.py',194),
  ('principal -> PRINCIPAL saveFunction LPAREN RPAREN LCURLY vars statements RCURLY','principal',8,'p_principal','main.py',199),
  ('statements -> assign SEMMICOLON statements','statements',3,'p_statements','main.py',208),
  ('statements -> functionCall SEMMICOLON statements','statements',3,'p_statements','main.py',209),
  ('statements -> read statements SEMMICOLON statements','statements',4,'p_statements','main.py',210),
  ('statements -> write statements SEMMICOLON statements','statements',4,'p_statements','main.py',211),
  ('statements -> for statements','statements',2,'p_statements','main.py',212),
  ('statements -> while statements','statements',2,'p_statements','main.py',213),
  ('statements -> if statements','statements',2,'p_statements','main.py',214),
  ('statements -> return statements','statements',2,'p_statements','main.py',215),
  ('statements -> empty','statements',1,'p_statements','main.py',216),
  ('assign -> ID add_id2 EQUALS saveOperator exp generateAssignQuad','assign',6,'p_assign','main.py',221),
  ('assign -> ID add_id2 arr EQUALS saveOperator exp generateAssignQuad','assign',7,'p_assign','main.py',222),
  ('generateAssignQuad -> <empty>','generateAssignQuad',0,'p_generateAssignQuad','main.py',226),
  ('add_id -> <empty>','add_id',0,'p_add_id','main.py',252),
  ('add_id2 -> <empty>','add_id2',0,'p_add_id2','main.py',264),
  ('functionCall -> ID LPAREN exp RPAREN','functionCall',4,'p_functionCall','main.py',280),
  ('media -> MEDIA LPAREN arr RPAREN SEMMICOLON','media',5,'p_media','main.py',285),
  ('read -> READ operatorRead LPAREN paramRead RPAREN','read',5,'p_read','main.py',294),
  ('paramRead -> paramReadAux','paramRead',1,'p_paramRead','main.py',299),
  ('paramRead -> empty','paramRead',1,'p_paramRead','main.py',300),
  ('paramReadAux -> exp generateQuadREAD','paramReadAux',2,'p_paramReadAux','main.py',305),
  ('paramReadAux -> exp generateQuadREAD COMMA operatorRead paramReadAux','paramReadAux',5,'p_paramReadAux','main.py',306),
  ('operatorRead -> <empty>','operatorRead',0,'p_operatorRead','main.py',311),
  ('generateQuadREAD -> <empty>','generateQuadREAD',0,'p_generateQuadREAD','main.py',318),
  ('write -> WRITE writeOperator LPAREN paramWrite RPAREN','write',5,'p_write','main.py',336),
  ('paramWrite -> paramWriteAux','paramWrite',1,'p_paramWrite','main.py',341),
  ('paramWrite -> empty','paramWrite',1,'p_paramWrite','main.py',342),
  ('paramWriteAux -> exp generateQuadPRINT','paramWriteAux',2,'p_paramWriteAux','main.py',347),
  ('paramWriteAux -> exp generateQuadPRINT COMMA writeOperator paramWriteAux','paramWriteAux',5,'p_paramWriteAux','main.py',348),
  ('writeOperator -> <empty>','writeOperator',0,'p_writeOperator','main.py',353),
  ('generateQuadPRINT -> <empty>','generateQuadPRINT',0,'p_generateQuadPRINT','main.py',360),
  ('LoopEnd -> <empty>','LoopEnd',0,'p_LoopEnd','main.py',377),
  ('for -> FOR forOP assign TO CTEI DO generateQuadFOR LCURLY statements RCURLY LoopEnd','for',11,'p_for','main.py',398),
  ('forOP -> <empty>','forOP',0,'p_forOP','main.py',403),
  ('generateQuadFOR -> <empty>','generateQuadFOR',0,'p_generateQuadFOR','main.py',411),
  ('while -> WHILE whileOP LPAREN exp RPAREN DO generateQuadWHILE LCURLY statements RCURLY LoopEnd','while',11,'p_while','main.py',429),
  ('whileOP -> <empty>','whileOP',0,'p_whileOP','main.py',434),
  ('generateQuadWHILE -> <empty>','generateQuadWHILE',0,'p_generateQuadWHILE','main.py',442),
  ('if -> IF LPAREN exp RPAREN generateQuadIF THEN LCURLY statements RCURLY else endIF','if',11,'p_if','main.py',464),
  ('else -> ELSE generateQuadELSE LCURLY statements RCURLY','else',5,'p_else','main.py',469),
  ('else -> empty','else',1,'p_else','main.py',470),
  ('generateQuadIF -> <empty>','generateQuadIF',0,'p_generateQuadIF','main.py',475),
  ('endIF -> <empty>','endIF',0,'p_endIF','main.py',492),
  ('generateQuadELSE -> <empty>','generateQuadELSE',0,'p_generateQuadELSE','main.py',500),
  ('exp -> nexp generateQuadOR','exp',2,'p_exp','main.py',544),
  ('exp -> nexp generateQuadOR OR saveOperator nexp','exp',5,'p_exp','main.py',545),
  ('generateQuadOR -> <empty>','generateQuadOR',0,'p_generateQuadOR','main.py',550),
  ('nexp -> compexp generateQuadAND','nexp',2,'p_nexp','main.py',560),
  ('nexp -> compexp generateQuadAND AND saveOperator compexp','nexp',5,'p_nexp','main.py',561),
  ('generateQuadAND -> <empty>','generateQuadAND',0,'p_generateQuadAND','main.py',566),
  ('compexp -> sumexp','compexp',1,'p_compexp','main.py',577),
  ('compexp -> compexp1 sumexp','compexp',2,'p_compexp','main.py',578),
  ('compexp1 -> sumexp GT saveOperator sumexp generateQuadCOMPARE','compexp1',5,'p_compexp1','main.py',583),
  ('compexp1 -> sumexp LT saveOperator sumexp generateQuadCOMPARE','compexp1',5,'p_compexp1','main.py',584),
  ('compexp1 -> sumexp GTE saveOperator sumexp generateQuadCOMPARE','compexp1',5,'p_compexp1','main.py',585),
  ('compexp1 -> sumexp LTE saveOperator sumexp generateQuadCOMPARE','compexp1',5,'p_compexp1','main.py',586),
  ('compexp1 -> sumexp NE saveOperator sumexp generateQuadCOMPARE','compexp1',5,'p_compexp1','main.py',587),
  ('generateQuadCOMPARE -> <empty>','generateQuadCOMPARE',0,'p_generateQuadCOMPARE','main.py',592),
  ('sumexp -> mulexp','sumexp',1,'p_sumexp','main.py',603),
  ('sumexp -> mulexp PLUS saveOperator mulexp generateQuadSUM','sumexp',5,'p_sumexp','main.py',604),
  ('sumexp -> mulexp MINUS saveOperator mulexp generateQuadSUM','sumexp',5,'p_sumexp','main.py',605),
  ('generateQuadSUM -> <empty>','generateQuadSUM',0,'p_generateQuadSUM','main.py',610),
  ('mulexp -> pexp','mulexp',1,'p_mulexp','main.py',621),
  ('mulexp -> pexp MUL saveOperator pexp generateQuadMUL','mulexp',5,'p_mulexp','main.py',622),
  ('mulexp -> pexp DIV saveOperator pexp generateQuadMUL','mulexp',5,'p_mulexp','main.py',623),
  ('generateQuadMUL -> <empty>','generateQuadMUL',0,'p_generateQuadMUL','main.py',628),
  ('pexp -> ID add_id2','pexp',2,'p_pexp','main.py',639),
  ('pexp -> CTEI saveCTE','pexp',2,'p_pexp','main.py',640),
  ('pexp -> CTEF saveCTE','pexp',2,'p_pexp','main.py',641),
  ('pexp -> CTEC saveCTE','pexp',2,'p_pexp','main.py',642),
  ('pexp -> CTESTRING saveCTE','pexp',2,'p_pexp','main.py',643),
  ('pexp -> functionCall','pexp',1,'p_pexp','main.py',644),
  ('pexp -> LPAREN exp RPAREN','pexp',3,'p_pexp','main.py',645),
  ('saveCTE -> <empty>','saveCTE',0,'p_saveCTE','main.py',650),
  ('saveOperator -> <empty>','saveOperator',0,'p_saveOperator','main.py',665),
  ('vars -> var','vars',1,'p_vars','main.py',678),
  ('vars -> empty','vars',1,'p_vars','main.py',679),
  ('var -> VARS var2','var',2,'p_var','main.py',684),
  ('var2 -> var2 type TWOPOINTS var1 SEMMICOLON addVar','var2',6,'p_var2','main.py',689),
  ('var2 -> empty','var2',1,'p_var2','main.py',690),
  ('var1 -> ID','var1',1,'p_var1','main.py',695),
  ('var1 -> ID COMMA var1 addVar','var1',4,'p_var1','main.py',696),
  ('var1 -> ID arr','var1',2,'p_var1','main.py',697),
  ('var1 -> ID arr COMMA var1 addVar','var1',5,'p_var1','main.py',698),
  ('var1 -> empty','var1',1,'p_var1','main.py',699),
  ('addVar -> <empty>','addVar',0,'p_addVar','main.py',706),
  ('saveTypeVar -> <empty>','saveTypeVar',0,'p_saveTypeVar','main.py',720),
  ('type -> INT saveTypeVar','type',2,'p_type','main.py',728),
  ('type -> CHAR saveTypeVar','type',2,'p_type','main.py',729),
  ('type -> FLOAT saveTypeVar','type',2,'p_type','main.py',730),
  ('arr -> LBRACKET CTEI RBRACKET','arr',3,'p_arr','main.py',735),
  ('arr -> LBRACKET exp RBRACKET','arr',3,'p_arr','main.py',736),
  ('functions -> FUNCTION INT functions1 functions','functions',4,'p_functions','main.py',745),
  ('functions -> FUNCTION CHAR functions1 functions','functions',4,'p_functions','main.py',746),
  ('functions -> FUNCTION FLOAT functions1 functions','functions',4,'p_functions','main.py',747),
  ('functions -> FUNCTION VOID functions1 functions','functions',4,'p_functions','main.py',748),
  ('functions -> empty','functions',1,'p_functions','main.py',749),
  ('functions1 -> ID saveFunction LPAREN args RPAREN vars LCURLY statements RCURLY','functions1',9,'p_functions1','main.py',754),
  ('functions1 -> empty','functions1',1,'p_functions1','main.py',755),
  ('saveFunction -> <empty>','saveFunction',0,'p_saveFunction','main.py',760),
  ('args -> args type TWOPOINTS var1 addVar','args',5,'p_args','main.py',771),
  ('args -> empty','args',1,'p_args','main.py',772),
  ('args1 -> ID addVar','args1',2,'p_args1','main.py',777),
  ('args1 -> ID COMMA args1','args1',3,'p_args1','main.py',778),
  ('args1 -> empty','args1',1,'p_args1','main.py',779),
  ('return -> RETURN LPAREN exp RPAREN SEMMICOLON','return',5,'p_return','main.py',784),
  ('return -> RETURN LPAREN exp RPAREN','return',4,'p_return','main.py',785),
  ('empty -> <empty>','empty',0,'p_empty','main.py',798),
]
