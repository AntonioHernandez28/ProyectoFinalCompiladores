import ply.lex as lex 
import ply.yacc as yacc 
import sys 

# Reserved Words 
reserved = {
    'program' : 'POGRAM', 
    'function' : 'FUNCION', 
    'vars' : 'VARS', 
    'void' : 'VOID', 
    'int' : 'INT', 
    'float' : 'FLOAT', 
    'char' : 'CHAR', 
    'main' : 'MAIN', 
    'if' : 'IF', 
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
    'varianza' : 'VARIANZA'
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
    'RCURLY'
] + list(reserved.values())

t_PLUS =  r'\+' 
t_MINUS = r'\-'
t_DIV = r'\/'
t_LT = r'\<'
t_GT = r'\>'
t_LTE = r'\<='
t_GTE = r'\>='
t_AND = r'\&&'
t_OR = r'\||'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r'\,'
t_SEMMICOLON = r'\;'
t_NE = r'\<>'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'

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