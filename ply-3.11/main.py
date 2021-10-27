import ply.lex as lex 
import ply.yacc as yacc 
from VariablesTable import VariablesTable, Var
from FunctionsDirectory import FunctionsDirectory
from SemanticCube import SemanticCube as Cube
from avail import Avail
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
    'COMPARE',
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
    'EQUALS', 
    'COMILLA'
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
t_COMILLA = r'\"'
t_COMPARE = r'\=='

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

NameStack = Stack()
TypeStack = Stack() 
OperatorsStack = Stack() 
Quads = []

avail = Avail()

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
    assign : ID add_id2 EQUALS saveOperator exp generateAssignQuad
            | ID add_id2 arr EQUALS saveOperator exp generateAssignQuad
    '''

def p_generateAssignQuad(p): 
    '''generateAssignQuad : '''
    global TypeStack, NameStack, OperatorsStack, Quads

    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '=': 
            CurrentOperator = OperatorsStack.pop() 
            RightOp = NameStack.pop() 
            RightType = TypeStack.pop() 
            LeftOp = NameStack.pop() 
            LeftType = TypeStack.pop() 

            #print('Left Type -> ', LeftType)
            #print('Right Type -> ', RightType)
            result = semanticCube.getType(LeftType, RightType, CurrentOperator)

            if result != 'ERROR': 
                currentQuad = (CurrentOperator, RightOp, None, LeftOp)
                print('Current Quad: ', str(currentQuad))
                Quads.append(currentQuad)
            
            else: 
                print('Type Dissmatch.')
                sys.exit()


def p_add_id(p): 
    ''' add_id : '''
    #print('ADD ID 1')
    global varID, functionsDirectory, FunctionID, NameStack, TypeStack
    if functionsDirectory.searchVariable(FunctionID, varID): 
        varType = functionsDirectory.getVarType(FunctionID, varID)
        if varType: 
            TypeStack.push(varType)
            NameStack.push(varID)

def p_add_id2(p): 
    ''' add_id2 : '''
    #print('ADD ID 2')
    global varID, functionsDirectory, FunctionID, NameStack, TypeStack
    varID = p[-1]
    print(varID)
    if functionsDirectory.searchVariable(FunctionID, varID): 
        types = functionsDirectory.getVarType(FunctionID, varID)
        TypeStack.push(types)
        NameStack.push(varID)
    
    else: 
        print('EXIT')
        SystemExit() 

def p_functionCall(p): 
    '''
    functionCall : ID LPAREN exp RPAREN
    '''

def p_read(p):
    '''
    read : READ operatorRead LPAREN var1 generateQuadREAD RPAREN 
    '''

def p_operatorRead(p): 
    '''
    operatorRead : 
    '''
    global OperatorsStack 
    OperatorsStack.push('read')

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
    write2 : COMILLA CTESTRING COMILLA
            | CTEI saveCTE generateQuadPRINT
            | CTEF saveCTE generateQuadPRINT
            | exp  
    '''
# ------------ End Statements ------------

# ------------- Cycles -------------
def p_for(p): 
    '''
    for : FOR forOP assign TO CTEI DO generateQuadFOR LCURLY statements RCURLY LoopEnd
    '''

def p_forOP(p): 
    '''
    forOP :
    '''
    global OperatorsStack, Quads, ConditionalJumpsStack
    OperatorsStack.push('for')
    ConditionalJumpsStack.push(len(Quads))

def p_generateQuadFOR(p): 
    '''
    generateQuadFOR :
    '''
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    ResultType = TypeStack.pop() 

    if ResultType == 'bool': 
        value = NameStack.pop() 
        currentQuad = ('GotoV', value, None, -1)
        print('Current Quad -> : ', str(currentQuad))
        Quads.append(currentQuad)
        ConditionalJumpsStack.push(len(Quads)-1)
    else: 
        print('Error in For Quad.')
        sys.exit() 
    
def p_LoopEnd(p): 
    '''
    LoopEnd :
    '''
    print('Entro aki')
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    End = ConditionalJumpsStack.pop() 
    Back = ConditionalJumpsStack.pop() 
    currentQuad = ('Goto', None, None, Back)
    print('Current Quad -> : ', str(currentQuad))
    Quads.append(currentQuad)
    FillQuad(End, -1)

def p_while(p):
    '''
    while : WHILE whileOP LPAREN exp RPAREN DO generateQuadWHILE LCURLY statements RCURLY LoopEnd
    '''

def p_whileOP(p): 
    '''
    whileOP : 
    '''
    global OperatorsStack, Quads, ConditionalJumpsStack
    OperatorsStack.push('while')
    ConditionalJumpsStack.push(len(Quads))

def p_generateQuadWHILE(p): 
    '''
    generateQuadWHILE :
    '''
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    ResultType = TypeStack.pop() 

    if ResultType == 'bool': 
        value = NameStack.pop()
        currentQuad = ('GotoF', value, None, -1)
        Quads.append(currentQuad)
        print('Current Quad -> : ', str(currentQuad))
        ConditionalJumpsStack.push(len(Quads)-1)
    else: 
        print('Error in While Quad.')
        sys.exit() 

# ------------ End Cycles -------------

# --------------- If ----------------
def p_if(p): 
    '''
    if : IF LPAREN exp RPAREN generateQuadIF THEN LCURLY statements RCURLY else endIF
    '''

def p_else(p): 
    '''
    else : ELSE generateQuadELSE LCURLY statements RCURLY
            | empty 
    '''
# ---------------- End If --------------

# ---------------- Expressions ----------------

def generateQuad(): 
    global OperatorsStack, NameStack, TypeStack, Quads 

    if OperatorsStack.size() > 0: 
        currentOperator = OperatorsStack.pop() 
        RightOp = NameStack.pop() 
        RightType = TypeStack.pop() 
        LeftOp = NameStack.pop() 
        LeftType = TypeStack.pop() 

        #print("-> ", LeftType) 

        typeResult = semanticCube.getType(LeftType, RightType, currentOperator)

        if typeResult != 'ERROR' : 
            result = avail.next() 
            currentQuad = (currentOperator, LeftOp, RightOp, result)
            print('Current Quad -> : ', str(currentQuad))
            Quads.append(currentQuad)
            NameStack.push(result)
            TypeStack.push(typeResult)
        
        else : 
            print('Type Dismatch.')
        
    else: 
        print('Operators Stack empty.')


def p_generateQuadOR(p): 
    '''
    generateQuadOR : 
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '|': 
            generateQuad() 

def p_generateQuadAND(p): 
    '''
    generateQuadAND : 
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '&&': 
            generateQuad()

def p_generateQuadCOMPARE(p): 
    '''
    generateQuadCOMPARE : 
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '<' or OperatorsStack.top() == '>' or OperatorsStack.top() == '<=' or OperatorsStack.top() == '>=' or OperatorsStack.top() == '==' or OperatorsStack.top() == '!=':
            generateQuad() 

def p_generateQuadIF(p): 
    '''
    generateQuadIF : 
    '''
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    typeResult = TypeStack.pop() 
    if typeResult == 'bool': 
        value = NameStack.pop() 
        currentQuad = ('GotoF', value, None, -1)
        print('Current Quad -> : ', str(currentQuad))
        Quads.append(currentQuad)
        ConditionalJumpsStack.push(len(Quads) -1)
    
    else: 
        print('Type Dismatch.') 
        return 

def p_generateQuadSUM(p): 
    '''
    generateQuadSUM :
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '+' or OperatorsStack.top() == '-': 
            generateQuad() 

def p_generateQuadMUL(p): 
    '''
    generateQuadMUL : 
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '*' or OperatorsStack.top() == '/': 
            generateQuad() 


def p_generateQuadPRINT(p): 
    '''
    generateQuadPRINT :
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == 'print': 
            OperatorAux = OperatorsStack.pop() 
            value = NameStack.pop() 
            TypeStack.pop() 
            currentQuad = (OperatorAux, None, None, value)
            print('Quad : ', str(currentQuad))
            Quads.append(currentQuad)


def p_generateQuadREAD(p): 
    '''
    generateQuadREAD : 
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == 'read': 
            OperatorAux = OperatorsStack.pop() 
            value = NameStack.pop() 
            TypeStack.pop() 
            currentQuad = (OperatorAux, None, None, value)
            print('Read Quad : ', str(currentQuad))
            Quads.append(currentQuad)

def p_endIF(p): 
    '''
    endIF : 
    '''
    global ConditionalJumpsStack 
    End = ConditionalJumpsStack.pop() 
    FillQuad(End, -1)

def p_generateQuadELSE(p): 
    '''
    generateQuadELSE :
    '''
    global Quads, ConditionalJumpsStack 
    currentQuad = ('Goto', None, None, -1)
    Quads.append(currentQuad)
    fAux = ConditionalJumpsStack.pop() 
    ConditionalJumpsStack.push(len(Quads)-1)
    FillQuad(fAux, -1)

def FillQuad(end, cont): 
    global Quads
    temp = list(Quads[end])
    temp[3] = len(Quads)
    Quads[end] = tuple(temp)
    print('Fill -> Quad', Quads[end])
        
    
def p_saveCTE(p): 
    ''' saveCTE : '''
    global cte, t 
    cte = p[-1]
    t = type(cte)
    if t == int:
        TypeStack.push('int')
        NameStack.push(cte)
    elif t == float: 
        TypeStack.push('float')
        NameStack.push(cte)
    else: 
        TypeStack.push('char')
        NameStack.push(cte)
 
def p_exp(p): 
    '''
    exp : nexp generateQuadOR
        | nexp generateQuadOR OR saveOperator nexp 
    '''

def p_nexp(p): 
    '''
    nexp : compexp generateQuadAND
        | compexp generateQuadAND AND saveOperator compexp 
    '''

def p_compexp(p): 
    '''
    compexp : sumexp 
            | compexp1 sumexp 
    '''

def p_compexp1(p): 
    '''
    compexp1 : sumexp GT saveOperator sumexp generateQuadCOMPARE
             | sumexp LT saveOperator sumexp generateQuadCOMPARE
             | sumexp GTE saveOperator sumexp generateQuadCOMPARE
             | sumexp LTE saveOperator sumexp generateQuadCOMPARE
             | sumexp NE saveOperator sumexp generateQuadCOMPARE
    '''

def p_sumexp(p): 
    '''
    sumexp : mulexp 
           | mulexp PLUS saveOperator mulexp generateQuadSUM 
           | mulexp MINUS saveOperator mulexp generateQuadSUM
    '''

def p_mulexp(p): 
    '''
    mulexp : pexp 
           | pexp MUL saveOperator pexp generateQuadMUL
           | pexp DIV saveOperator pexp generateQuadMUL
    '''

def p_pexp(p):
    '''
    pexp : var1 add_id
         | CTEI saveCTE
         | CTEF saveCTE
         | CTEC saveCTE
         | CTESTRING saveCTE
         | functionCall 
         | LPAREN exp RPAREN 
    '''
    

def p_saveOperator(p): 
    ''' saveOperator : '''
    global OperatorsStack 
    currentOperator = p[-1]
    OperatorsStack.push(currentOperator)
    #print("Operator saved: ", OperatorsStack.top())    

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
    #print("Current Type Var: ", currentTypeVar)

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
    functions1 : ID saveFunction LPAREN args RPAREN vars LCURLY statements RCURLY  
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
    args : args type TWOPOINTS var1 addVar
         | empty 
    '''

def p_args1(p): 
    '''
    args1 : ID addVar
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
        fileName = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\ply-3.11\\test2.txt'
        currentFile = open(fileName, 'r')
        print("Current File is: " + fileName)
        info = currentFile.read() 
        currentFile.close()
        lexer.input(info)
        while True: 
            tok = lexer.token() 
            if not tok: 
                break 
           # print(tok)
        if(parser.parse(info, tracking=True) == 'COMPILED'): 
            print("CORRECT SYNTAX")
        else: 
            print("SYNTAX ERROR")
    
    except EOFError: 
        print(EOFError)

main()

