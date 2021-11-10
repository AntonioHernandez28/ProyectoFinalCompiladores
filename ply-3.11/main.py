import ply.lex as lex 
import ply.yacc as yacc 
from VariablesTable import VariablesTable, Var
from FunctionsDirectory import FunctionsDirectory
from SemanticCube import SemanticCube as Cube
from avail import Avail
from stack import Stack
import sys 
import os



# =====================================================================
# ---------------------------- RESERVED WORDS ----------------------
# =====================================================================

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

# =====================================================================
# ------------------------------- TOKENS ----------------------------
# =====================================================================

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

# =====================================================================
# --------------------- INITIALIZE STACKS AND TABLES -----------------
# =====================================================================

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
CountParams = 0 
JumpEndProcess = 0 
pending = 0 
EndProcess = []
Functions = []
paramID = '' 
firstParam = 0
# =====================================================================
# --------------------------- GRAMMAR RULES --------------------------
# =====================================================================

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
    FunctionID = 'program'

    if functionsDirectory.searchFunction(FunctionID): 
        print("Function already exists.")
    else: 
        functionsDirectory.addFunction(currentFunctionType, FunctionID, 0, [], [], 0)
        print("Function added: ", FunctionID, " | Type: ", currentFunctionType)

        


def p_program1(p): 
    '''
    program1 : vars mainQuad functions mainEnd program2
            | vars mainQuad functions 
            | program2
    '''

def p_program2(p): 
    '''
    program2 : principal
    '''

def p_principal(p): 
    '''
    principal : PRINCIPAL saveFunction LPAREN RPAREN LCURLY vars statements RCURLY 
    '''

def p_mainQuad(p): 
    '''
    mainQuad : 
    '''
    global ConditionalJumpsStack, Quads 
    currentQuad = ('GOTOPRINCIPAL', 'PRINCIPAL', -1, None)
    Quads.append(currentQuad)
    ConditionalJumpsStack.push(len(Quads)-1)

def p_mainEnd(p): 
    '''
    mainEnd : 
    '''
    End = ConditionalJumpsStack.pop() 
    FillQuad(End, -1)

# =====================================================================
# --------------------------- STATEMENTS --------------------------
# =====================================================================

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
    print(varID)
    if not varID == None: 
        if functionsDirectory.searchVariable(FunctionID, varID): 
            varType = functionsDirectory.getVarType(FunctionID, varID)
            if varType: 
                TypeStack.push(varType)
                NameStack.push(varID)
        else: 
            sys.exit()


def p_add_id2(p): 
    ''' add_id2 : '''
    #print('ADD ID 2')
    global varID, functionsDirectory, FunctionID, NameStack, TypeStack
    varID = p[-1]
    print("El var ID en save ID es: ", varID)
    if not varID == None: 
        if functionsDirectory.searchVariable(FunctionID, varID): 
            types = functionsDirectory.getVarType(FunctionID, varID)
            TypeStack.push(types)
            NameStack.push(varID)
    
        else: 
            print('EXIT')
            sys.exit()

# add ID for manage arrays but need to be checked !!!!!!!!!!!!!!!!!
def p_add_id3(p): 
    ''' add_id3 : '''
    #print('ADD ID 2')
    global varID, functionsDirectory, FunctionID, NameStack, TypeStack
    varID = p[-2]
    print("El var ID en save ID es: ", varID)
    if not varID == None: 
        if functionsDirectory.searchVariable(FunctionID, varID): 
            types = functionsDirectory.getVarType(FunctionID, varID)
            TypeStack.push(types)
            NameStack.push(varID)
    
        else: 
            print('EXIT')
            sys.exit()  


def p_media(p): 
    '''
    media : MEDIA LPAREN arr RPAREN SEMMICOLON
    '''


# =====================================================================
# -------------------------- FUNCTION CALLS --------------------------
# =====================================================================

def p_functionCall(p): 
    '''
    functionCall : ID functionERA LPAREN expAux generateQuadPARAM RPAREN generateQuadGOSUB 
    '''

def p_generateQuadPARAM(p): 
    '''
    generateQuadPARAM : 
    '''
    global Quads, CountParams, nameVar, callID, pending 
    callID = p[-4]
    print("Call ID: ", callID)
    totalParams = functionsDirectory.getNumberParameters(callID)
    print("Total Params: ", totalParams)
    
    if not NameStack.empty(): 
        value = NameStack.pop() 
        print("Value Param: ", value)
        if not CountParams == totalParams: 
            print("Parameter updated number: ", CountParams)
            CurrentQuad = ('PARAM', value, None, -1)
            Quads.append(CurrentQuad)
            OperatorsStack.push('PARAM')
            NameStack.pop() 
            CountParams += 1 


def p_expAux(p): 
    '''
    expAux : exp 
           | exp COMMA expAux 
           | empty  
    '''


def p_generateQuadGOSUB(p): 
    '''
    generateQuadGOSUB :
    '''
    global Quads, Functions, JumpEndProcess
    gosubCall = p[-6] #-5? 
    CurrentQuad = ('GOSUB', None, None, gosubCall)
    Quads.append(CurrentQuad)

def p_fillEndProc(p): 
    '''
    fillEndProc : 
    '''
    global EndProcess, JumpEndProcess 
    End = EndProcess.pop() 
    Temp = list(Quads[End])
    Temp[3] = JumpEndProcess
    Quads[End] = tuple(Temp)

def p_functionERA(p):
    '''
    functionERA : 
    '''
    global Quads, CountParams, nameVar 
    nameVar = p[-1]
    CurrentQuad = ('ERA', None, None, nameVar)
    Quads.append(CurrentQuad) 

# =====================================================================
# -------------------------------- READ -----------------------------
# =====================================================================

def p_read(p):
    '''
    read : READ operatorRead LPAREN paramReadAux RPAREN 
    '''

def p_paramRead(p): 
    '''
    paramRead : paramReadAux 
              | empty 
    '''

def p_paramReadAux(p): 
    '''
    paramReadAux : exp generateQuadREAD 
                 | exp generateQuadREAD COMMA operatorRead paramReadAux 
    '''

def p_operatorRead(p): 
    '''
    operatorRead : 
    '''
    global OperatorsStack 
    OperatorsStack.push('read')

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

# =====================================================================
# -------------------------------- WRITE -----------------------------
# =====================================================================

def p_write(p): 
    '''
    write : WRITE writeOperator LPAREN paramWrite RPAREN
    '''

def p_paramWrite(p): 
    '''
    paramWrite : paramWriteAux 
               | empty 
    '''

def p_paramWriteAux(p): 
    '''
    paramWriteAux : exp generateQuadPRINT 
                  | exp generateQuadPRINT COMMA writeOperator paramWriteAux 
    '''

def p_writeOperator(p): 
    '''
    writeOperator : 
    '''
    global OperatorsStack
    OperatorsStack.push('write')

def p_generateQuadPRINT(p): 
    '''
    generateQuadPRINT :
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == 'write': 
            OperatorAux = OperatorsStack.pop() 
            value = NameStack.pop() 
            TypeStack.pop() 
            currentQuad = (OperatorAux, None, None, value)
            print('Quad : ', str(currentQuad))
            Quads.append(currentQuad)

# =====================================================================
# -------------------------------- LOOPS -----------------------------
# =====================================================================
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

def FillQuad(end, cont): #Used in IF section too. 
    global Quads
    temp = list(Quads[end])
    temp[3] = len(Quads)
    Quads[end] = tuple(temp)
    print('Fill -> Quad', Quads[end])

# FOR LOOP 
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

# WHILE LOOP
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

    
# =====================================================================
# -------------------------------- IF ------------------------------
# =====================================================================

def p_if(p): 
    '''
    if : IF LPAREN exp RPAREN generateQuadIF THEN LCURLY statements RCURLY else endIF
    '''

def p_else(p): 
    '''
    else : ELSE generateQuadELSE LCURLY statements RCURLY
            | empty 
    '''

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

# =====================================================================
# ------------------------------ EXPRESSIONS -------------------------
# =====================================================================

def generateQuad(): 
    global OperatorsStack, NameStack, TypeStack, Quads 

    if OperatorsStack.size() > 0: 
        currentOperator = OperatorsStack.pop() 
        RightOp = NameStack.pop() 
        RightType = TypeStack.pop() 
        LeftOp = NameStack.pop() 
        LeftType = TypeStack.pop() 

        print("-> ", RightType) 

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

# OR 
def p_exp(p): 
    '''
    exp : nexp generateQuadOR
        | nexp generateQuadOR OR saveOperator nexp 
    '''

def p_generateQuadOR(p): 
    '''
    generateQuadOR : 
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '|': 
            generateQuad() 

# AND 
def p_nexp(p): 
    '''
    nexp : compexp generateQuadAND
        | compexp generateQuadAND AND saveOperator compexp 
    '''

def p_generateQuadAND(p): 
    '''
    generateQuadAND : 
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '&&': 
            generateQuad()


# COMPARE 
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

def p_generateQuadCOMPARE(p): 
    '''
    generateQuadCOMPARE : 
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '<' or OperatorsStack.top() == '>' or OperatorsStack.top() == '<=' or OperatorsStack.top() == '>=' or OperatorsStack.top() == '==' or OperatorsStack.top() == '!=':
            generateQuad() 


# SUM 
def p_sumexp(p): 
    '''
    sumexp : mulexp 
           | mulexp PLUS saveOperator mulexp generateQuadSUM 
           | mulexp MINUS saveOperator mulexp generateQuadSUM
    '''

def p_generateQuadSUM(p): 
    '''
    generateQuadSUM :
    '''
    global OperatorsStack
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '+' or OperatorsStack.top() == '-': 
            generateQuad() 


# MUL 
def p_mulexp(p): 
    '''
    mulexp : pexp 
           | pexp MUL saveOperator pexp generateQuadMUL
           | pexp DIV saveOperator pexp generateQuadMUL
    '''

def p_generateQuadMUL(p): 
    '''
    generateQuadMUL : 
    '''
    global OperatorsStack 
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '*' or OperatorsStack.top() == '/': 
            generateQuad() 


# Constants And ID's 
def p_pexp(p):
    '''
    pexp : ID add_id2
         | CTEI saveCTE
         | CTEF saveCTE
         | CTEC saveCTE
         | CTESTRING saveCTE
         | functionCall 
         | LPAREN exp RPAREN 
         | ID arr add_id3
         | empty
    '''   

def p_saveCTE(p): 
    ''' saveCTE : '''
    print("Entro al CTE")
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

def p_saveOperator(p): 
    ''' saveOperator : '''
    global OperatorsStack 
    currentOperator = p[-1]
    OperatorsStack.push(currentOperator)
    print("Operator saved: ", OperatorsStack.top())      


# =====================================================================
# --------------------------------- VARS ---------------------------
# =====================================================================

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
    print("Current ID -> ", varID)
    

def p_addVar(p): 
    'addVar :'
    global functionsDirectory 
    global varID 
    global currentTypeVar

    if not varID == None:
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

# =====================================================================
# ---------------------------- FUNCTIONS -----------------------------
# =====================================================================

def p_functions(p): 
    '''
    functions : FUNCTION INT functions1 endFunc functions 
              | FUNCTION CHAR functions1 endFunc functions 
              | FUNCTION FLOAT functions1 endFunc functions 
              | FUNCTION VOID functions1 endFunc functions 
              | empty
    '''

def p_functions1(p): 
    '''
    functions1 : ID saveFunction LPAREN parameters RPAREN vars LCURLY statements RCURLY  
               | empty
    '''

#Fix bug with multiple params. 
def p_addParameter(p): 
    '''
    addParameter : 
    '''
    global functionsDirectory, paramID, firstParam, currentTypeVar
    paramID = p[-1]
    firstParam = 1 
    print("paramID: ", paramID)
    print("Function ID: ", FunctionID)
    if not paramID == None: 
        if functionsDirectory.searchFunction(FunctionID): 
            print("Entro aki")
            functionsDirectory.addParameters(FunctionID, paramID, currentTypeVar)
            functionsDirectory.addVariable(FunctionID, currentTypeVar, paramID)
        else:
            sys.exit() 

def p_parameters(p): 
    '''
    parameters : paramsAux 
                | empty 
    '''

def p_paramsAux(p): 
    '''
    paramsAux : INT saveTypeVar TWOPOINTS ID addParameter nextParam 
              | FLOAT saveTypeVar TWOPOINTS ID addParameter nextParam 
              | CHAR saveTypeVar TWOPOINTS ID addParameter nextParam 
    '''

def p_nextParam(p): 
    '''
    nextParam : COMMA paramsAux 
                | empty 
    '''



def p_endFunc(p): 
    '''
    endFunc : 
    '''
    global Quads 
    CurrentQuad = ('ENDFUNC', None, None, -1)
    Quads.append(CurrentQuad)

def p_saveFunction(p): 
    '''
    saveFunction : 
    '''
    global currentFunctionType
    currentFunctionType = p[-2]
    global FunctionID
    FunctionID = p[-1]
    global functionsDirectory
    print("Entra en el crash")
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

# =====================================================================
# --------------------------- ERROR HANDLER --------------------------
# =====================================================================

def p_error(p):
    print("Syntax error in: ", p) 
    sys.exit() 


def p_empty(p): 
    '''
    empty :  
    '''
    p[0] = None 

parser = yacc.yacc()

# =====================================================================
# ------------------------------- MAIN ------------------------------
# =====================================================================

def main(): 
    try: 
        fileName = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\ply-3.11\\test3.txt'
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
        cont = 0 
        for i in Quads: 
            print('Final Quad #', cont, ' : ', str(i))
            cont = cont + 1
    
    except EOFError: 
        print(EOFError)

main()

