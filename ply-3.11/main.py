import ply.lex as lex 
import ply.yacc as yacc 
from VariablesTable import VariablesTable, Var
from FunctionsDirectory import FunctionsDirectory
from SemanticCube import SemanticCube as Cube
from stack import Stack
import sys 
import os

# Reserved Words 
reserved = {
    'Program' : 'PROGRAM', 
    'function' : 'FUNCTION', 
    'VARS' : 'VARS', 
    'void' : 'VOID', 
    'int' : 'INT', 
    'float' : 'FLOAT', 
    'char' : 'CHAR', 
    'principal' : 'PRINCIPAL', 
    'if' : 'IF', 
    'then' : 'THEN',
    'else' : 'ELSE', 
    'read' : 'READ',
    'write' : 'WRITE', 
    'return' : 'RETURN', 
    'end' : 'END', 
    'for' : 'FOR', 
    'from' : 'FROM', 
    'while' : 'WHILE', 
    'to' : 'TO',
    'media' : 'MEDIA', 
    'moda' : 'MODA', 
    'varianza' : 'VARIANZA',
    'simpleregression' : 'SIMPLEREGRESSION', 
    'plotxy' : 'PLOTXY', 
    'do' : 'DO'
}

# Tokens 
tokens = [
    'ID', 
    'CTEI', #Constante Integer 
    'CTEC', #Constante Char
    'CTEF', #Constante Float
    'CTESTRING', #Constante String 
    'PLUS', 
    'MINUS', 
    'DIV', 
    'MUL',
    'LT',
    'GT', 
    'LTE', #Less than or equal
    'GTE', #Greater than or equal
    'AND',
    'OR', 
    'LPAREN',
    'RPAREN', 
    'COMMA', 
    'SEMMICOLON', 
    'NE', 
    'LBRACKET',
    'RBRACKET', 
    'LCURLY', 
    'RCURLY', 
    'TWOPOINTS', 
    'EQUALS'
] + list(reserved.values())

t_PLUS =  r'\+' 
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_LT = r'\<'
t_GT = r'\>'
t_LTE = r'\<='
t_GTE = r'\>='
t_AND = r'\&&'
t_OR = r'\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMMICOLON = r'\;'
t_NE = r'\<>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_TWOPOINTS = r'\:'
t_EQUALS = r'\='
t_ignore = ' \t\n'

# Identify ID's 
def t_ID(t): 
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t 

# Identify Integer Constants 
def t_CTEI(t): 
    r'0|[-+]?[1-9][0-9]*'
    t.value = int(t.value) 
    return t 

# Identify Float Constants 
def t_CTEF(t): 
    r'[-+]?\d*\.\d+'
    t.value = float(t.value)
    return t 

# Identify String Constants 
def t_CTESTRING(t): 
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t 


# Handle Errors
def t_error(t): 
    print("ERROR at '%s'" % t.value)
    t.lexer.skip(1) 

lexer = lex.lex()

functionsDirectory = FunctionsDirectory() 
currentFunctionType = ''
FunctionID = '' 
oper_name_types = Stack()

VarsNameStack = Stack()
VarsTypeStack = Stack() 
OperatorsStack = Stack() 
Quads = []

semanticCube = Cube()
ConditionalJumpsStack = Stack()

########################## Grammar Rules ###############################

def p_program(p): 
    '''
    program : PROGRAM ID SEMMICOLON addProgram program1 
    '''
    p[0] = 'COMPILED'

def p_addProgram(p): 
    '''
    addProgram :
    ''' 
    global FunctionID 
    global currentFunctionType 
    global functionsDirectory

    currentFunctionType = 'program'
    ProgramID = p[-2]
    FunctionID = ProgramID

    if functionsDirectory.searchFunction(FunctionID): 
        print("Function already exists.")
    else: 
        functionsDirectory.addFunction(currentFunctionType, FunctionID, 0, [], [], 0)
        print("Function added: ", FunctionID, " | Type: ", currentFunctionType)

        


def p_program1(p): 
    '''
    program1 : vars functions program2
            | vars functions 
            | program2
    '''

def p_program2(p): 
    '''
    program2 : principal
    '''

def p_principal(p): 
    '''
    principal : PRINCIPAL LPAREN RPAREN LCURLY vars statements RCURLY 
    '''
    global currentFunctionType
    currentFunctionType = p[1]
    global FunctionID
    FunctionID = p[1]
    global functionsDirectory

    functionsDirectory.addFunction(currentFunctionType, FunctionID, 0, [], [], 0)

# -------------- Statements --------------
def p_statements(p): 
    '''
    statements : assign SEMMICOLON statements 
        | functionCall SEMMICOLON statements 
        | read statements SEMMICOLON statements
        | write statements SEMMICOLON statements 
        | for statements 
        | while statements 
        | if statements 
        | return statements
        | empty
    '''


def p_assign(p): 
    '''
    assign : ID add_id EQUALS exp
            | ID add_id arr EQUALS exp 
    '''

def p_add_id(p): 
    ''' add_id : '''
    
    global varID, functionsDirectory, FunctionID
    varID = p[-1]
    if functionsDirectory.searchVariable(FunctionID, varID): 
        varType = functionsDirectory.getVarType(FunctionID, varID)
        currentVar = Var(varType, varID)
        oper_name_types.push(currentVar)
    else: 
        sys.exit()

def p_functionCall(p): 
    '''
    functionCall : ID LPAREN exp RPAREN
    '''

def p_read(p):
    '''
    read : READ LPAREN read1 RPAREN 
    '''

def p_read1(p): 
    '''
    read1 : ID read2 
    '''

def p_read2(p): 
    '''
    read2 : COMMA read1 
        | empty
    '''

def p_media(p): 
    '''
    media : MEDIA LPAREN arr RPAREN SEMMICOLON
    '''

def p_write(p): 
    '''
    write : WRITE LPAREN write1 RPAREN
    '''

def p_write1(p): 
    '''
    write1 : write2 COMMA write2 
            | write2 
    '''

def p_write2(p): 
    '''
    write2 : CTESTRING
            | CTEI 
            | CTEF
            | exp 
    '''
# ------------ End Statements ------------

# ------------- Cycles -------------
def p_for(p): 
    '''
    for : FOR assign TO CTEI DO LCURLY statements RCURLY 
    '''

def p_while(p):
    '''
    while : WHILE LPAREN exp RPAREN DO LCURLY statements RCURLY 
    '''

# ------------ End Cycles -------------

# --------------- If ----------------
def p_if(p): 
    '''
    if : IF LPAREN exp RPAREN THEN LCURLY statements RCURLY else 
    '''

def p_else(p): 
    '''
    else : ELSE LCURLY statements RCURLY
            | empty 
    '''
# ---------------- End If --------------

# ---------------- Expressions ----------------

def p_exp(p): 
    '''
    exp : nexp 
        | nexp OR nexp 
    '''

def p_nexp(p): 
    '''
    nexp : compexp 
        | compexp AND compexp 
    '''

def p_compexp(p): 
    '''
    compexp : sumexp 
            | compexp1 sumexp 
    '''

def p_compexp1(p): 
    '''
    compexp1 : sumexp GT saveOperator sumexp 
             | sumexp LT saveOperator sumexp 
             | sumexp GTE saveOperator sumexp 
             | sumexp LTE saveOperator sumexp 
             | sumexp NE saveOperator sumexp 
    '''

def p_sumexp(p): 
    '''
    sumexp : mulexp 
           | mulexp PLUS saveOperator mulexp 
           | mulexp MINUS saveOperator mulexp 
    '''

def p_mulexp(p): 
    '''
    mulexp : pexp 
           | pexp MUL saveOperator pexp 
           | pexp DIV saveOperator pexp  
    '''

def p_pexp(p):
    '''
    pexp : var1 
         | CTEI 
         | CTEF 
         | functionCall 
         | LPAREN exp RPAREN 
    '''

def p_saveOperator(p): 
    ''' saveOperator : '''
    global currentOperator 
    currentOperator = p[-1]
    OperatorsStack.push(currentOperator)
    print(OperatorsStack.top())    

# ---------------- END Expressions ------------

# ----------------- Vars rules ----------------

def p_vars(p): 
    '''
    vars : var
        | empty
    '''

def p_var(p): 
    '''
    var : VARS var2 
    ''' 

def p_var2(p): 
    '''
    var2 : var2 type TWOPOINTS var1 SEMMICOLON addVar
         | empty 
    '''

def p_var1(p):
    '''
    var1 : ID 
         | ID COMMA var1 addVar
         | ID arr 
         | ID arr COMMA var1 addVar
         | empty 
    '''
    global varID 
    varID = p[1]

def p_addVar(p): 
    'addVar :'
    global functionsDirectory 
    global varID 
    global currentTypeVar

    if functionsDirectory.searchFunction(FunctionID): 
        functionsDirectory.addVariable(FunctionID, currentTypeVar, varID)
        varDatos = Var(currentTypeVar, varID)
        oper_name_types.push(varDatos)
    else: 
        SystemExit()

def p_saveTypeVar(p): 
    '''
    saveTypeVar : 
    '''
    global currentTypeVar 
    currentTypeVar = p[-1]
    print("Current Type Var: ", currentTypeVar)

def p_type(p): 
    '''
    type : INT saveTypeVar
         | CHAR saveTypeVar
         | FLOAT saveTypeVar 
    '''

def p_arr(p): 
    '''
    arr : LBRACKET CTEI RBRACKET 
        | LBRACKET exp RBRACKET
    '''

# -------------- Functions ------------


def p_functions(p): 
    '''
    functions : FUNCTION INT functions1 functions
              | FUNCTION CHAR functions1 functions
              | FUNCTION FLOAT functions1 functions
              | FUNCTION VOID functions1 functions
              | empty
    '''

def p_functions1(p): 
    '''
    functions1 : ID saveFunction LPAREN args RPAREN vars LCURLY statements RCURLY functions1 
               | empty
    '''

def p_saveFunction(p): 
    '''
    saveFunction : 
    '''
    global currentFunctionType
    currentFunctionType = p[-2]
    global FunctionID
    FunctionID = p[-1]
    global functionsDirectory
    functionsDirectory.addFunction(currentFunctionType, FunctionID, 0, [], [], 0)

def p_args(p): 
    '''
    args : type TWOPOINTS args1
         | empty 
    '''

def p_args1(p): 
    '''
    args1 : ID 
          | ID COMMA args1 
          | empty 
    '''

def p_return(p): 
    '''
    return : RETURN LPAREN exp RPAREN SEMMICOLON
            | RETURN LPAREN exp RPAREN 
    '''

# ------------- End Functions ---------------

# Error handling 

def p_error(p):
    print("Sintax error in: ", p) 


def p_empty(p): 
    '''
    empty :  
    '''
    p[0] = None 
    

parser = yacc.yacc()


def main(): 
    try: 
        fileName = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\ply-3.11\\test.txt'
        currentFile = open(fileName, 'r')
        print("Current File is: " + fileName)
        info = currentFile.read() 
        currentFile.close()
        lexer.input(info)
        while True: 
            tok = lexer.token() 
            if not tok: 
                break 
            print(tok)
        if(parser.parse(info, tracking=True) == 'COMPILED'): 
            print("CORRECT SYNTAX")
        else: 
            print("SYNTAX ERROR")
    
    except EOFError: 
        print(EOFError)

main()

