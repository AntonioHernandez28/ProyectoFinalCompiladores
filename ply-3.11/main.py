from typing import Type
from numpy.core.fromnumeric import mean, var
import ply.lex as lex 
import ply.yacc as yacc 
from VariablesTable import VariablesTable, Var
from FunctionsDirectory import FunctionsDirectory
from memory import Memory
from SemanticCube import SemanticCube as Cube
from avail import Avail
from stack import Stack
import sys 
from Quadruples import Quadruples
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
    'do' : 'DO',
    'sort' : 'SORT',
    'mean' : 'MEAN',
    'find' : 'FIND', 
    'mode' : 'MODE', 
    'variance' : 'VARIANCE', 
    'plot' : 'PLOT'
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
    'COMILLA',
    #'DOT'
] + list(reserved.values())

t_PLUS =  r'\+' 
t_MINUS = r'\-'
t_DIV = r'\/'
t_MUL = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMPARE = r'=='
t_EQUALS = r'\='
t_LCURLY = r'\{'
t_RCURLY = r'\}'
t_AND = r'\&&'
t_OR = r'\|'
t_TWOPOINTS = r'\:'
t_SEMMICOLON = r'\;'
t_COMMA = r'\,'
t_LTE = r'\<='
t_GTE = r'\>='
t_LT = r'\<'
t_GT = r'\>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMILLA = r'\"'
t_NE = r'\<>'
t_ignore = ' \t\n'

# Identify ID's 
def t_ID(t): 
    r'[A-Za-z]+[A-Za-z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t 

# Identify Float Constants 
def t_CTEF(t): 
    r'\d+(\.)\d+'
    t.value = float(t.value)
    return t

# Identify Integer Constants 
def t_CTEI(t): 
    r'\d+'
    t.value = int(t.value) 
    return t 


# Identify String Constants 
def t_CTESTRING(t): 
    r'\'[\w\d\s\,. ]*\'|\"[\w\d\s\,. ]*\"'
    return t 


# Handle Errors
def t_error(t): 
    print("ERROR at '%s'" % t.value[0])
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
Quads = Quadruples()
FinalQuads = None 
ConstTable = []  
arraySize = []
avail = Avail()
Quads2 = []
stackArrays = []

semanticCube = Cube()
ConditionalJumpsStack = Stack()
ReturnJumpStack = Stack() 
CountParams = 0 
JumpEndProcess = 0 
pending = 0 
EndProcess = []
Functions = []
paramID = '' 
firstParam = 0
isEmpty = False 
callID = ''
tempCounter = 0 
memory = Memory()
tempDictionary = {} 
constantTable = []
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
    global funType

    currentFunctionType = 'program'
    FunctionID = 'program'
    funType = currentFunctionType

    if functionsDirectory.searchFunction(FunctionID): 
        print("Function already exists.")
    else: 
        functionsDirectory.addFunction(currentFunctionType, FunctionID, 0, [], [], -1, 0, 0)
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
    currentOp = memory.getOperatorCode('GOTOPRINCIPAL')
    currentQuad = (currentOp, 'PRINCIPAL', -1, None)
    Quads.addQuad(currentOp, 'PRINCIPAL', -1, None)
    Quads2.append(currentQuad)
    ConditionalJumpsStack.push(len(Quads.quadruples)-1)

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
        | return SEMMICOLON statements 
        | sort statements SEMMICOLON statements 
        | plot statements SEMMICOLON statements
        | empty
    '''

def p_assign(p): 
    '''
    assign : ID add_id2 EQUALS saveOperator exp generateAssignQuad
            | ID arrStatement EQUALS saveOperator exp generateAssignQuad
            | ID add_id2 EQUALS saveOperator functionCall generateAssignQuad
            | ID add_id2 EQUALS saveOperator mean generateAssignQuad
            | ID add_id2 EQUALS saveOperator find generateAssignQuad
            | ID add_id2 EQUALS saveOperator mode generateAssignQuad
            | ID add_id2 EQUALS saveOperator variance generateAssignQuad
    '''

def p_generateAssignQuad(p): 
    '''generateAssignQuad : '''
    global TypeStack, NameStack, OperatorsStack, Quads, FunctionID
    print("ENTRO AL ASIGN DESPUES DEL MEAN!!!")
    OperatorsStack.print()
    if OperatorsStack.size() > 0: 
        if OperatorsStack.top() == '=': 
            print("Entro al yamerito ")
            CurrentOperator = OperatorsStack.pop() 
            RightOp = NameStack.pop() 
            RightType = TypeStack.pop() 
            LeftOp = NameStack.pop() 
            LeftType = TypeStack.pop() 

            print('Left Type -> ', LeftType)
            print('Right Type -> ', RightType)
            result = semanticCube.getType(LeftType, RightType, CurrentOperator)

            if result != 'ERROR': 
                #RightOpAddress = functionsDirectory.getDirectionById(FunctionID, RightOp)
                #LeftOpAddress = functionsDirectory.getDirectionById(FunctionID, LeftOp)
                currOperator = memory.getOperatorCode(CurrentOperator)
                print("Right Address: ", RightOp)
                currentQuad = (currOperator, RightOp, None, LeftOp)
                print('Current Quad: ', str(currentQuad))
                Quads.addQuad(currOperator, RightOp, None, LeftOp)
                Quads2.append(currentQuad)
            
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
    varAddress = functionsDirectory.getDirectionById(FunctionID, varID)
    if not varID == None: 
        if functionsDirectory.searchVariable(FunctionID, varID): 
            types = functionsDirectory.getVarType(FunctionID, varID)
            print("METIO EL: ", types )
            TypeStack.push(types)
            NameStack.push(varAddress)
    
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
            print("NAMESTACK")
            NameStack.print()
    
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
    functionCall : ID validateFunctionID functionERA LPAREN expAux verifyParams RPAREN generateQuadGOSUB 
    '''
    global callID 
    callID = p[1]
    print("Current Call ID: ", callID)

def p_validateFunctionID(p): 
    '''
    validateFunctionID : 
    '''
    global callID 
    callID = p[-1]
    print("Enters to validate: ", p[-1])
    currentFuncID = p[-1]
    if(functionsDirectory.searchFunction(currentFuncID)): 
        print("Function Exists, go ahead :) ")
        TypeStack.print()
    else: 
        print("Function does NOT exist.")
        sys.exit() 

def p_verifyParams(p): 
    '''
    verifyParams :
    '''
    global CountParams, callID 
    print("Get into verify params")
    print("Current Call ID in Verify Params: ", callID)
    totalParams = functionsDirectory.getNumberParameters(callID)
    print("Total Params: ", totalParams)
    print("Count Params: ", CountParams)
    if(totalParams != CountParams): 
        print("Parameters provided does NOT match expected ones.")
        sys.exit() 
    
    CountParams = 0
    print("PERRU")
    TypeStack.print() 



def p_paramsCount(p): 
    '''
    paramsCount : 
    '''
    global CountParams
    CountParams += 1
    print("Cont is: ", CountParams)
    print("Updated Params: ", CountParams)

def p_generateQuadPARAM(p): 
    '''
    generateQuadPARAM : 
    '''
    global Quads, CountParams, callID, FunctionID 
    argument = NameStack.pop() 
    currentType = TypeStack.pop()
    print("Argument: ", argument)
    print("Tipo: ", currentType)
    expectedParams = functionsDirectory.getParamsTypes(callID)
    nameParams = functionsDirectory.getParamsNames(callID)
    print("LOS PARAMS")
    print(nameParams[CountParams])
    print("Busko un: ", argument)
    arg = functionsDirectory.getDirectionById(FunctionID, argument)
    print("El ARG es: ", arg)
    print("FUN ID ES: ", FunctionID)
    print(nameParams[0])
    print("I am looking for a: ", nameParams[CountParams])

    if CountParams >= len(expectedParams):
        print("Params size does NOT match expected one. Compiler was expecting # ", len(expectedParams), " parameters.") 
        sys.exit()

    if currentType != expectedParams[CountParams]: 
        print("Param Type does NOT match the expected one. Compiler was expecting type: ", expectedParams[CountParams])
        sys.exit()
    currOperator = memory.getOperatorCode('PARAM')
    currentQuad = (currOperator, arg, argument, 'PARAM#' + str(CountParams + 1))
    print(currentQuad)
    Quads.addQuad(currOperator, arg, argument, 'PARAM#' + str(CountParams+1))
    Quads2.append(currentQuad)

    


def p_expAux(p): 
    '''
    expAux : exp generateQuadPARAM paramsCount
           | exp generateQuadPARAM COMMA paramsCount expAux 
           | empty  
    '''


def p_generateQuadGOSUB(p): 
    '''
    generateQuadGOSUB :
    '''
    global Quads, Functions, callID
    gosubCall = p[-6] #-5? 
    operator = memory.getOperatorCode('GOSUB')
    CurrentQuad = (operator, callID, None, functionsDirectory.getDirection(callID))
    Quads.addQuad(operator, callID, None, functionsDirectory.getDirection(callID))
    Quads2.append(CurrentQuad)
    currentFuncType = functionsDirectory.getFunctionType(callID)
    print("CURRENT TAIP: ", currentFuncType)
    if currentFuncType != 'void': 
        TypeStack.push(currentFuncType)
        temporalAddress = memory.assignMemory('temps', currentFuncType)
        NameStack.push(temporalAddress)
        TypeStack.push(currentFuncType)
        NameStack.push(functionsDirectory.getGlobalVar(callID))
        TypeStack.push(currentFuncType)
        OperatorsStack.push('=')
        p_generateAssignQuad(p)
        NameStack.push(temporalAddress)
        TypeStack.push(currentFuncType)

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
    global Quads, CountParams, nameVar, paramsK 
    nameVar = p[-2]
    currentOp = memory.getOperatorCode('ERA')
    CurrentQuad = (currentOp, None, None, nameVar)
    Quads.addQuad(currentOp, None, None, nameVar)
    Quads2.append(CurrentQuad) 
    print("PERRIO")
    TypeStack.print() 
    

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
            currentOp = memory.getOperatorCode(OperatorAux)
            value = NameStack.pop() 
            TypeStack.pop() 
            currentQuad = (currentOp, None, None, value)
            print('Read Quad : ', str(currentQuad))
            Quads.addQuad(currentOp, None, None, value)
            Quads2.append(currentQuad)

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
            currentOp = memory.getOperatorCode(OperatorAux)
            value = NameStack.pop() 
            TypeStack.pop() 
            currentQuad = (currentOp, None, None, value)
            print('Quad : ', str(currentQuad))
            Quads.addQuad(currentOp, None, None, value)
            Quads2.append(currentQuad)


# =====================================================================
# -------------------------------- SORT -----------------------------
# =====================================================================

def p_sort(p): 
    '''
    sort : SORT sortOperator LPAREN ID add_id2 verifyArray  RPAREN generateQuadSORT 
    '''
    print("BRRRR")

def p_sortOperator(p): 
    '''
    sortOperator : 
    '''
    global OperatorsStack
    OperatorsStack.push('sort')

def p_verifyArray(p): 
    '''verifyArray : '''
    global FunctionID, varID, currArray 
    currID = p[-2]
    currArray = currID
    print("El ID es en verifai arrei: ", currID)
    print("Lo que kiero comparar antes del crash: ", functionsDirectory.getSizeForArray(FunctionID, currID))
    if functionsDirectory.getSizeForArray(FunctionID, currID) <= 0: 
        print("The variable: ", currID, " is NOT an array, so it can not be sorted.")
        sys.exit() 
    else: 
        varID = currID
    
def p_generateQuadSORT(p): 
    '''
    generateQuadSORT : 
    '''
    global OperatorsStack, varID, FunctionID 
    if OperatorsStack.size() > 0: 
        OperatorAux = OperatorsStack.pop()
        currOperator = 'SORT' 
        value = NameStack.pop()
        sizeArray = functionsDirectory.getSizeForArray(FunctionID, varID)
        currQuad = ('SORT', value, None, sizeArray)
        currOp = memory.getOperatorCode('sort')
        Quads2.append(currQuad)
        Quads.addQuad(currOp, value, None, sizeArray)



# =====================================================================
# -------------------------------- FIND  -----------------------------
# =====================================================================

def p_find(p): 
    '''
    find : FIND findOperator LPAREN ID add_id2 verifyArray COMMA ID add_id2 RPAREN generateQuadFIND
    '''

def p_findOperator(p): 
    '''
    findOperator : 
    '''
    global OperatorsStack
    print("CHEK4")
    OperatorsStack.push('find')

def p_generateQuadFIND(p): 
    '''
    generateQuadFIND : 
    '''
    print("BRBR: ", p[-7])
    global varID, TypeStack, FunctionID, OperatorsStack
    FindAddress = memory.assignMemory('global', 'float')
    TypeStack.pop()
    TypeStack.pop()
    functionsDirectory.addVariable('program', 'float', 'find', FindAddress)
    sizeArray = functionsDirectory.getSizeForArray(FunctionID, p[-7])
    valueToFind = NameStack.pop()
    arrDirection = NameStack.pop()
    print("Value to find: ", valueToFind)
    print("Array Direction: ", arrDirection)
    currentQ = ('FIND', arrDirection, valueToFind, FindAddress, sizeArray)
    Quads2.append(currentQ)
    currOp = OperatorsStack.pop()
    currOp = memory.getOperatorCode(currOp)
    Quads.addQuad(currOp, {'startDirection' : arrDirection, 'valueToFind' : valueToFind}, FindAddress, sizeArray)
    TypeStack.push('int')
    NameStack.push(FindAddress)

# =====================================================================
# -------------------------------- MEAN -----------------------------
# =====================================================================

def p_mean(p): 
    '''
    mean : MEAN meanOperator LPAREN ID add_id2 verifyArray RPAREN generateQuadMEAN 
         | empty
    '''

def p_meanOperator(p): 
    '''
    meanOperator : 
    '''
    global OperatorsStack 
    OperatorsStack.push('mean')

def p_generateQuadMEAN(p): 
    '''
    generateQuadMEAN :
    '''
    global varID, TypeStack, FunctionID
    meanAddress = memory.assignMemory('global', 'float')
    TypeStack.pop()
    functionsDirectory.addVariable('program', 'float', 'mean', meanAddress)
    sizeArray = functionsDirectory.getSizeForArray(FunctionID, varID)
    value = NameStack.pop()
    CurrQuad = ('Mean', value, meanAddress, sizeArray)
    Quads2.append(CurrQuad)
    print("CURR MEAN QUAD: -> ", str(CurrQuad))
    oper = OperatorsStack.pop()
    TypeStack.push('float')
    currOp = memory.getOperatorCode(oper)
    Quads.addQuad(currOp, value, meanAddress, sizeArray)
    NameStack.push(meanAddress)
    


# =====================================================================
# -------------------------------- MODE -----------------------------
# =====================================================================

def p_mode(p): 
    '''
    mode : MODE modeOperator LPAREN ID add_id2 verifyArray RPAREN generateQuadMODE
         | empty
    '''

def p_modeOperator(p): 
    '''
    modeOperator : 
    '''
    global OperatorsStack 
    OperatorsStack.push('mode')

def p_generateQuadMODE(p): 
    '''
    generateQuadMODE :
    '''
    global varID, TypeStack, FunctionID
    meanAddress = memory.assignMemory('global', 'float')
    TypeStack.pop()
    functionsDirectory.addVariable('program', 'float', 'mode', meanAddress)
    sizeArray = functionsDirectory.getSizeForArray(FunctionID, varID)
    value = NameStack.pop()
    CurrQuad = ('Mode', value, meanAddress, sizeArray)
    Quads2.append(CurrQuad)
    print("CURR MODE QUAD: -> ", str(CurrQuad))
    oper = OperatorsStack.pop()
    TypeStack.push('float')
    currOp = memory.getOperatorCode(oper)
    Quads.addQuad(currOp, value, meanAddress, sizeArray)
    NameStack.push(meanAddress)
    


# =====================================================================
# -------------------------------- VARIANCE -----------------------------
# =====================================================================

def p_variance(p): 
    '''
    variance : VARIANCE varianceOperator LPAREN ID add_id2 verifyArray RPAREN generateQuadVARIANCE
         | empty
    '''

def p_varianceOperator(p): 
    '''
    varianceOperator : 
    '''
    global OperatorsStack 
    OperatorsStack.push('variance')

def p_generateQuadVARIANCE(p): 
    '''
    generateQuadVARIANCE :
    '''
    global varID, TypeStack, FunctionID
    meanAddress = memory.assignMemory('global', 'float')
    TypeStack.pop()
    functionsDirectory.addVariable('program', 'float', 'variance', meanAddress)
    sizeArray = functionsDirectory.getSizeForArray(FunctionID, varID)
    value = NameStack.pop()
    CurrQuad = ('variance', value, meanAddress, sizeArray)
    Quads2.append(CurrQuad)
    print("CURR VAR QUAD: -> ", str(CurrQuad))
    oper = OperatorsStack.pop()
    TypeStack.push('float')
    currOp = memory.getOperatorCode(oper)
    Quads.addQuad(currOp, value, meanAddress, sizeArray)
    NameStack.push(meanAddress)
    

# =====================================================================
# -------------------------------- PLOT -----------------------------
# =====================================================================

def p_plot(p): 
    '''
    plot : PLOT plotOperator LPAREN ID add_id2 verifyArray saveIDaux COMMA ID add_id2 verifyArrayForPlot RPAREN generateQuadPLOT 
    '''
    print("BRRRR")

def p_plotOperator(p): 
    '''
    plotOperator : 
    '''
    global OperatorsStack
    OperatorsStack.push('plot')

def p_saveIDaux(p):
    '''
    saveIDaux : 
    '''
    global auxID, varID 
    auxID = varID

def p_verifyArrayForPlot(p): 
    '''verifyArrayForPlot : '''
    global FunctionID, currArray, varID 
    print("AL VER ARR X PLOT ES: ", varID)
    currID = p[-2]
    currArray = currID
    print("El ID es en verifai arrei2: ", currID)
    print("Lo que kiero comparar antes del crash: ", functionsDirectory.getSizeForArray(FunctionID, currID))
    if functionsDirectory.getSizeForArray(FunctionID, currID) <= 0: 
        print("The variable: ", currID, " is NOT an array, so it can not be sorted.")
        sys.exit() 
    else: 
        varID = currID
    
def p_generateQuadPLOT(p): 
    '''
    generateQuadPLOT : 
    '''
    global OperatorsStack, varID, FunctionID, auxID
    print("EL VARID 1 es: ", auxID)
    print("El varID2 es: ", varID)
    if OperatorsStack.size() > 0: 
        OperatorAux = OperatorsStack.pop()
        currOperator = 'PLOT' 
        value = NameStack.pop()
        value2 = NameStack.pop()
        sizeArray1 = functionsDirectory.getSizeForArray(FunctionID, auxID)
        sizeArray2 = functionsDirectory.getSizeForArray(FunctionID, varID)
        if sizeArray1 != sizeArray2: 
            print("For plotting, both arrays need to be same size.")
            sys.exit()

        currQuad = ('PLOT', value, value2, sizeArray1, sizeArray2)
        currOp = memory.getOperatorCode('plot')
        Quads2.append(currQuad)
        Quads.addQuad(currOp, value, value2, {'SizeArray1' : sizeArray1, 'SizeArray2' : sizeArray2})

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
    currentOp = memory.getOperatorCode('Goto')
    currentQuad = (currentOp, None, None, Back)
    print('Current Quad -> : ', str(currentQuad))
    Quads.addQuad(currentOp, None, None, Back)
    Quads2.append(currentQuad)
    FillQuad(End, -1)

def FillQuad(end, cont): #Used in IF section too. 
    global Quads
    print("ENTRO AL FILL BOY: ", end)
    tempQuad = Quads.getQuadByAddress(end)
    Quads.updateQuad(tempQuad['operator'], tempQuad['leftOp'], tempQuad['rightOp'], len(Quads.quadruples), end)
    temp = list(Quads2[end])
    temp[3] = len(Quads2)
    Quads2[end] = tuple(temp)
    print('Fill -> Quad', Quads.quadruples[end])


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
    ConditionalJumpsStack.push(len(Quads.quadruples))

def p_generateQuadFOR(p): 
    '''
    generateQuadFOR :
    '''
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    ResultType = TypeStack.pop() 

    if ResultType == 'bool': 
        value = NameStack.pop() 
        currOp = memory.getOperatorCode('GotoV')
        currentQuad = (currOp, value, None, -1)
        print('Current Quad -> : ', str(currentQuad))
        Quads.addQuad(currOp, value, None, -1)
        Quads2.append(currentQuad)
        ConditionalJumpsStack.push(len(Quads.quadruples)-1)
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
    ConditionalJumpsStack.push(len(Quads.quadruples))

def p_generateQuadWHILE(p): 
    '''
    generateQuadWHILE :
    '''
    global NameStack, TypeStack, Quads, ConditionalJumpsStack
    ResultType = TypeStack.pop() 

    if ResultType == 'bool': 
        value = NameStack.pop()
        currOp = memory.getOperatorCode('GotoF')
        currentQuad = (currOp, value, None, -1)
        Quads.addQuad(currOp, value, None, -1)
        Quads2.append(currentQuad)
        print('Current Quad -> : ', str(currentQuad))
        ConditionalJumpsStack.push(len(Quads.quadruples)-1)
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
        currOp = memory.getOperatorCode('GotoF')
        currentQuad = (currOp, value, None, -1)
        print('Current Quad -> : ', str(currentQuad))
        Quads.addQuad(currOp, value, None, -1)
        Quads2.append(currentQuad)
        ConditionalJumpsStack.push(len(Quads.quadruples) -1)
    
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
    currOp = memory.getOperatorCode('Goto')
    currentQuad = (currOp, None, None, -1)
    Quads.addQuad(currOp, None, None, -1)
    Quads2.append(currentQuad)
    fAux = ConditionalJumpsStack.pop() 
    ConditionalJumpsStack.push(len(Quads.quadruples)-1)
    FillQuad(fAux, -1)

# =====================================================================
# ------------------------------ EXPRESSIONS -------------------------
# =====================================================================

def generateQuad(): 
    global OperatorsStack, NameStack, TypeStack, Quads, tempCounter, tempDictionary 

    if OperatorsStack.size() > 0: 
        currentOperator = OperatorsStack.pop() 
        RightOp = NameStack.pop() 
        RightType = TypeStack.pop() 
        LeftOp = NameStack.pop() 
        LeftType = TypeStack.pop() 

        print("los que llegan son: ", LeftOp, " y el: ", RightOp)

        currOperator = memory.getOperatorCode(currentOperator)

        typeResult = semanticCube.getType(LeftType, RightType, currentOperator)

        if typeResult != 'ERROR' : 
            result = avail.next() 
            tempAddress = memory.assignMemory('temps', typeResult)
            #memory.setAddressTemp(result, tempAddress)
            tempCounter += 1
            print("El temp es: ", tempAddress)
            
            currentQuad = (currOperator, LeftOp, RightOp, tempAddress)
            print('Current Quad -> : ', str(currentQuad))
            Quads.addQuad(currOperator, LeftOp, RightOp, tempAddress)
            Quads2.append(currentQuad)
            NameStack.push(tempAddress)
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
             | sumexp COMPARE saveOperator sumexp generateQuadCOMPARE
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
         | functionCallExp 
         | LPAREN exp RPAREN 
         | ID arrStatement 
         | empty
    '''   

def p_functionCallExp(p): 
    '''
    functionCallExp : ID LPAREN validateFunctionIDexp functionERA expAux verifyParams RPAREN generateQuadGOSUB 
    '''
    global callID 
    callID = p[-2]
    print("Current Call ID: ", callID)

def p_validateFunctionIDexp(p): 
    '''
    validateFunctionIDexp : 
    '''
    global callID 
    callID = p[-2]
    print("Enters to validate: ", p[-1])
    currentFuncID = p[-2]
    if(functionsDirectory.searchFunction(currentFuncID)): 
        print("Function Exists, go ahead :) ")
        TypeStack.print()
    else: 
        print("Function does NOT exist.")
        sys.exit() 

def p_arrStatement(p): 
    '''
    arrStatement : LBRACKET checkArray exp generateQuadVER RBRACKET getArrFinalAddress
                | empty
    '''

def p_getArrFinalAddress(p): 
    '''
    getArrFinalAddress :
    '''
    print("Acaba con array")
    global FunctionID, varID, currArray
    arg = NameStack.pop() 
    print("EL VAR ID ES EN FINAL ADDRESS: ", currArray)
    baseDirection = functionsDirectory.getDirectionById(FunctionID, currArray)
    currOperator = memory.getOperatorCode('+')
    arrType = functionsDirectory.getVarType(FunctionID, varID)
    tempAddress = memory.assignMemory('pointers', arrType)
    if not searchConstant(baseDirection): 
        virtualAddress = memory.assignMemory('constants', 'int')
        constantTable.append(
        {
            'constant' : baseDirection, 
            'address' : virtualAddress
        }
        )
    else: 
        virtualAddress = getConstantAddress(baseDirection)

    Quads.addQuad(currOperator, arg, virtualAddress, tempAddress)
    CurrentQuad = ('+', arg, baseDirection, tempAddress)
    Quads2.append(CurrentQuad)
    NameStack.print()
    NameStack.push(tempAddress)
    TypeStack.push(arrType)
    print("Temp address es: ", tempAddress)
    NameStack.print()
    currArray = ''

def p_checkArray(p): 
    '''
    checkArray : 
    '''
    global FunctionID, varID, currArray 
    currID = p[-2]
    currArray = currID
    print("El ID es: ", currID)
    print("Lo que kiero comparar antes del crash: ", functionsDirectory.getSizeForArray(FunctionID, currID))
    if functionsDirectory.getSizeForArray(FunctionID, currID) <= 0: 
        print("The variable: ", currID, " is NOT an array, so it can not be indexed.")
        sys.exit() 
    else: 
        varID = currID

def p_generateQuadVER(p): 
    '''
    generateQuadVER : 
    '''
    global FunctionID, varID, currArray
    print("El varID que le llega es: ", varID)
    arg = NameStack.top()
    print("IN VER el arg es: ", arg)
    bound = functionsDirectory.getSizeForArray(FunctionID, currArray)
    if not searchConstant(0): 
        address = memory.assignMemory('constants', 'int')
        constantTable.append({
            'constant': 0, 
            'address' : address
        })
    opCode = memory.getOperatorCode('VER')
    currentQuad = (opCode, arg, getConstantAddress(0), getConstantAddress(bound))
    Quads2.append(currentQuad)
    Quads.addQuad(opCode, arg, getConstantAddress(0), getConstantAddress(bound))
    print("QUAD VER ADDED WITH: ", arg, " and 0 y: ", bound)


def searchConstant(constant): 
    for const in constantTable: 
        if const['constant'] == constant: 
            return True 
    return False

def getConstantAddress(constant): 
    for const in constantTable: 
        if const['constant'] == constant: 
            return const['address']
    print("Constant not found.")

def p_saveCTE(p): # Dont forget check string fixes in memory !!!!!!!!!!!!!!!!!!
    ''' saveCTE : '''
    print("Entro al CTE")
    global cte, t 
    cte = p[-1]
    t = type(cte)

    if t == int:
        TypeStack.push('int')
        if not searchConstant(cte): 
            virtualAddress = memory.assignMemory('constants', 'int')
            constantTable.append(
                {
                    'constant' : cte, 
                    'address' : virtualAddress
                }
            )
            print("Constant added.")
        else: 
            virtualAddress = getConstantAddress(cte)
        NameStack.push(virtualAddress)
    elif t == float: 
        TypeStack.push('float')
        if not searchConstant(cte): 
            virtualAddress = memory.assignMemory('constants', 'int')
            constantTable.append(
                {
                    'constant' : cte, 
                    'address' : virtualAddress
                }
            )
        else: 
            virtualAddress = getConstantAddress(cte)
        NameStack.push(virtualAddress)
    else: 
        TypeStack.push('char')
        if not searchConstant(cte): 
            virtualAddress = memory.assignMemory('constants', 'int')
            constantTable.append(
                {
                    'constant' : cte, 
                    'address' : virtualAddress
                }
            )
        else: 
            virtualAddress = getConstantAddress(cte)
        NameStack.push(virtualAddress)
    
    

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
         | ID createArr arr 
         | ID createArr arr COMMA var1 addVar
         | empty 
    '''
    global varID 
    varID = p[1]
    print("Current ID -> ", varID)


def p_createArr(p): 
    '''
    createArr : 
    '''
    global arrID, stackArrays
    arrID = p[-1]
    print("DETECTO EL ARRAY: ", arrID)
    stackArrays.append(arrID)
    #stackArrays.print()
    
    

       
def p_addVar(p): 
    'addVar :'
    global functionsDirectory 
    global varID 
    global currentTypeVar
    global arraySize
    global arrID
    global stackArrays
    global isArray
    context = ''
    
    if(FunctionID == 'program'): 
        virtualAddress = memory.assignMemory('global', currentTypeVar)
        context = 'global'
    else: 
        virtualAddress = memory.assignMemory('local', currentTypeVar)
        context = 'local'
    
    print("Se registró: ", varID, " con dirección en -> ", virtualAddress, " | en la funcion -> ", FunctionID)
    if not varID == None:
        if functionsDirectory.searchFunction(FunctionID): 
            functionsDirectory.addVariable(FunctionID, currentTypeVar, varID, virtualAddress)
            varDatos = Var(currentTypeVar, varID)
            oper_name_types.push(varDatos)
        else: 
            SystemExit()

    if len(stackArrays) > 0: 
        if stackArrays[len(stackArrays)-1] == varID:
            print("DATA ARREI")
            print(stackArrays)
            print(arraySize)
            currSize = arraySize.pop()
            memory.assignMemoryToArray(context, currentTypeVar, currSize)
            functionsDirectory.printFunctionVariables(FunctionID)
            functionsDirectory.setSizeForArray(FunctionID, varID, currSize)
            stackArrays.pop()

    

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
    arr : LBRACKET CTEI setArraySize RBRACKET 
    '''

def p_setArraySize(p):
    '''
    setArraySize : 
    '''
    print("Aqui entro el pendejo")
    global arrID, arraySize
    cte = p[-1]
    if cte <= 0: 
        print("Array size must be greater than zero.")
        sys.exit()
    if not searchConstant(cte): 
        virtualAddress = memory.assignMemory('constants', 'int')
        constantTable.append(
        {
            'constant' : cte, 
            'address' : virtualAddress
        }
        )
    arraySize.append(cte)
        


# =====================================================================
# ---------------------------- FUNCTIONS -----------------------------
# =====================================================================

def p_functions(p): 
    '''
    functions : FUNCTION INT saveFunType functions2 endFunc functions 
              | FUNCTION CHAR saveFunType functions2 endFunc functions 
              | FUNCTION FLOAT saveFunType functions2 endFunc functions 
              | FUNCTION VOID saveFunType functions1 endFunc functions 
              | empty
    '''

def p_saveFunType(p): 
    '''
    saveFunType :
    '''
    global funType 
    funType = p[-1]

def p_functions1(p): 
    '''
    functions1 : ID saveFunction LPAREN parameters RPAREN vars LCURLY setStartDirection statements RCURLY  
               | empty
    '''

def p_functions2(p): 
    '''
    functions2 : ID saveFunction LPAREN parameters RPAREN vars LCURLY setStartDirection statements RCURLY  
               | empty
    '''

def p_setStartDirection(p): 
    '''
    setStartDirection : 
    '''
    global FunctionID 
    print("Global ID in start Direction is: ", FunctionID)
    functionsDirectory.setStartDir(FunctionID, len(Quads.quadruples)) 

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
            virtualAddress = memory.assignMemory('local', currentTypeVar)
            functionsDirectory.addParameters(FunctionID, paramID, currentTypeVar)
            functionsDirectory.addVariable(FunctionID, currentTypeVar, paramID, virtualAddress)
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
    global Quads, tempCounter, FunctionID, functionsDirectory
    while ReturnJumpStack.size() > 0: 
        End = ReturnJumpStack.pop()
        FillQuad(End, -1)
    currentOp = memory.getOperatorCode('ENDFUNC')
    CurrentQuad = (currentOp, None, None, -1)
    Quads.addQuad(currentOp, None, None, -1)
    Quads2.append(CurrentQuad)
    currentVars = functionsDirectory.getNumberVars(FunctionID)
    print("Vars Number in ", FunctionID, " are: ", functionsDirectory.getNumberVars(FunctionID)) # Vars already has params and vars 
    print("Param number are: ", functionsDirectory.getNumberParameters(FunctionID))
    print("Temps are: ", tempCounter)
    functionsDirectory.setTotalSize(FunctionID, currentVars + tempCounter)
    memory.cleanLocalMemory() 
    avail.clear() 
    tempCounter = 0


def p_saveFunction(p): 
    '''
    saveFunction : 
    '''
    global currentFunctionType, functionsDirectory, FunctionID, funType
    FunctionID = p[-1]
    print("FUN TAIP: ", currentFunctionType)
    if funType != 'void' and funType != 'program':
        print("AL menos llego a criko")
        tempAddress = memory.assignMemory('global', funType)
        print("Sere menso: ", FunctionID)
        functionsDirectory.addVariable('program', currentTypeVar, FunctionID, tempAddress)
    print("Entra en el crash")
    functionsDirectory.addFunction(funType, FunctionID, 0, [], [], -1, 0, 0)
    global arrID 
    arrID = None
    

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
    return : RETURN LPAREN exp generateQuadRETURN RPAREN 
    '''

def p_generateQuadRETURN(p): 
    '''
    generateQuadRETURN : 
    '''
    print("CHICOOS")
    global funType
    operand = NameStack.pop()
    operandType = TypeStack.pop()
    returnAddress = functionsDirectory.getGlobalVar(FunctionID)
    if funType != operandType: 
        print("Type dismatch, return of this function must be: ", funType)
        sys.exit()
    else: 
        currQuad = ('RETURN', returnAddress, None, operand)
        Quads2.append(currQuad)
        opCode = memory.getOperatorCode('RETURN')
        Quads.addQuad(opCode, returnAddress, None, operand)
        opCodeGoto = memory.getOperatorCode('Goto')
        currQuad = ('GOTO', None, None, -1)
        Quads2.append(currQuad)
        Quads.addQuad(opCodeGoto, None, None, -1)
        ReturnJumpStack.push(len(Quads.quadruples)-1)
        print("SE METIO ALGO AL RETURN JUMP")
        ReturnJumpStack.print()

    

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
    global functionsDirectory
    try: 
        fileName = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\ply-3.11\\factorialCycle.txt'
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
        for i in Quads2: 
            print('Final Quad #', cont, ' : ', str(i))
            cont = cont + 1
        functionsDirectory.printFunction('program')
    
    except EOFError: 
        print(EOFError)
    
FinalQuads = Quads 
ConstTable = constantTable
#finalFuncDirectory = functionsDirectory
#main()

