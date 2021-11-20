# File for running 
import Quadruples 
from main import parser, FinalQuads, ConstTable
from main import lexer
import json 
import sys 

def exportQuads(file): 
    OutputFile = open(file, "w") 
    quads = FinalQuads.quadruples 
    for quad in quads: 
        quad = json.dumps(quad) 
        OutputFile.write(str(quad) + '\n')

def exportConstants(file): 
    OutputFile = open(file, "w") 
    consts = ConstTable
    for const in consts: 
        const = json.dumps(const)
        OutputFile.write(str(const) + '\n')

def main(): 
    file2open = 'c:\\Users\\ajhr9\\Documents\\Last Semester\\Compiladores\\Proyecto Minino++\\ProyectoFinalCompiladores\\ply-3.11\\test4.txt'
    file = open(file2open, 'r')
    code = file.read() 
    parser.parse(code, tracking=True)
    exportQuads("quads.txt")
    exportConstants("consts.txt")

main()


    