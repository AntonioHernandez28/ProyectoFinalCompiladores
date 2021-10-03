import ply.lex as lex 
import ply.yacc as yacc 
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


########################## Grammar Rules ###############################

def p_program(p): 
    '''
    program : PROGRAM ID SEMMICOLON program1 
    '''
    p[0] = 'COMPILED'

def p_program1(p): 
    '''
    program1 : vars functions principal
            | vars functions 
            | program2
    '''

def p_program2(p): 
    '''
    program2 : principal
    '''

def p_principal(p): 
    '''
    principal : PRINCIPAL LPAREN RPAREN LCURLY statements RCURLY 
    '''

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
    assign : ID EQUALS exp
            | ID LBRACKET exp RBRACKET EQUALS exp 
    '''

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
    exp : ID BasicExp exp
        | arr BasicExp exp
        | expCons BasicExp exp 
        | ID 
        | functionCall
        | ID LBRACKET exp RBRACKET
        | expCons 
    '''

def p_expCons(p): 
    '''
    expCons : CTEI 
            | CTEF  
    '''

def p_BasicExp(p): 
    '''
    BasicExp : PLUS 
            | MINUS 
            | MUL 
            | DIV 
            | GTE 
            | LTE 
            | LT 
            | GT 
    '''

# ---------------- END Expressions ------------

# ----------------- Vars rules ----------------

def p_vars(p): 
    '''
    vars : VARS var1
        | empty
    '''

def p_var1(p): 
    '''
    var1 : type TWOPOINTS ID MultipleVars SEMMICOLON var2
    '''

def p_var2(p): 
    '''
    var2 : var1 
        | empty 
    '''


def p_MultipleVars(p): 
    '''
    MultipleVars : COMMA ID MultipleVars
                | COMMA ID LBRACKET CTEI RBRACKET MultipleVars
                | empty 
    '''

def p_type(p): 
    '''
    type : INT 
        | CHAR 
        | FLOAT 
    '''

def p_arr(p): 
    '''
    arr : LBRACKET CTEI RBRACKET 
        | LBRACKET exp RBRACKET
    '''

# -------------- Functions ------------

def p_functions(p): 
    '''
    functions : FUNCTION VOID functionVoid functions 
                | FUNCTION type functionType functions
                | empty
    '''

def p_functionVoid(p): 
    '''
    functionVoid : ID LPAREN args RPAREN vars LCURLY statements RCURLY 
    '''

def p_functionType(p): 
    '''
    functionType : ID LPAREN args RPAREN vars LCURLY statements return SEMMICOLON RCURLY
    '''

def p_args(p): 
    '''
    args : type TWOPOINTS ID MultipleArgs 
        | empty 
    '''

def p_MultipleArgs(s): 
    '''
    MultipleArgs : COMMA args 
        | empty 
    '''

def p_return(s): 
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

