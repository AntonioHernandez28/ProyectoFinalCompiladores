from OperationHandler import OperationHandler
import json 
import sys 

operations = OperationHandler()
operators = {
            '+' : 1, 
            '-' : 2, 
            '*' : 3, 
            '/' : 4, 
            '<' : 5, 
            '>' : 6, 
            '<=' : 7, 
            '>=' : 8, 
            '==' : 9, 
            '!=' : 10,
            '&&' : 11, 
            '|' : 12, 
            '=' : 13, 
            'for' : 14, 
            'while' : 15, 
            'read' : 16, 
            'write' : 17,
            'GOTOPRINCIPAL' : 18, 
            'ENDFUNC' : 19, 
            'ERA' : 20, 
            'PARAM' : 21, 
            'GOSUB' : 22, 
            'Goto' : 23, 
            'GotoF' : 24, 
            'GotoV' : 25, 
            'VER' : 26
        }

hashMapHandler = {
    1 : operations.plusOperator, 
    2 : operations.minusOperator, 
    3 : operations.multOperator, 
    4 : operations.divOperator, 
    5 : operations.lessOperator, 
    6 : operations.greaterOperator, 
    7 : operations.lessEqOperator, 
    8 : operations.greaterEqOperator, 
    9 : operations.equalOperator, 
    10 : operations.notEqualOperator, 
    11 : operations.andOperator, 
    12 : operations.orOperator, 
    13 : operations.assign, 
    14 : None, 
    15 : None, 
    16 : operations.read, 
    17 : operations.write, 
    18 : operations.goto, 
    19 : operations.endProc, 
    20 : operations.era, 
    21 : operations.param, 
    22 : operations.gosub, 
    23 : operations.goto, 
    24 : operations.gotoFalse, 
    25 : operations.gotoTrue, 
    26 : operations.ver
}

quadruples = []
quadCounter = 0 

def main(): 
    global quadCounter

    file2open = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\quads.txt'
    file2open2 = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\consts.txt'
    file = open(file2open, 'r')
    fileConst = open(file2open2, 'r')
    lines = file.readlines() 
    consts = fileConst.readlines()
    file.close()
    fileConst.close()

    for line in lines: 
        line = json.loads(line)
        quadruples.append(line)
    
    operations.loadConstantTable(consts)

    while quadCounter < len(quadruples): 
        #print("Entro a los quad we")
        print(quadruples[quadCounter]['operator'])
        newQuadNumber = hashMapHandler[quadruples[quadCounter]['operator']](quadruples[quadCounter])
        if newQuadNumber: 
            quadCounter = newQuadNumber
        else: 
            quadCounter += 1

main()







