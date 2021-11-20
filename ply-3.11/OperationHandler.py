from VirtualMemory import VirtualMemory
from stack import Stack
import numpy as np 
import json 
import sys 

class OperationHandler: 
    def __int__(self): 
        self.virtualMemory = VirtualMemory()
        self.jumpStack = Stack() 
    
    def loadConstantTable(self, constants): 
        for i in constants: 
            currentConstant = json.loads(i)
            self.virtualMemory.updateMemory(
                currentConstant['constant'],
                currentConstant['virtualAddress']
            )
        
    def assign(self, quad): 
        leftOp = quad['leftOp']
        result = quad['result']
        self.virtualMemory.updateMemory(
            result, 
            self.virtualMemory.getValue(leftOp)
        )
    
    def write(self, quad): 
        value = self.virtualMemory.getValue(
            quad['result']
        )
        print(value)
    
    def read(self, quad): 
        value = input()
        try: 
            val = int(value)
        except ValueError: 
            try: 
                val = float(value)
            except: 
                val = value 
        result = quad['result']
        self.virtualMemory.updateMemory(
            result, 
            val
        )
    
    def goto(self, quad): 
        return quad['result']
    
    def gotoFalse(self, quad): 
        if not self.virtualMemory.getValue(quad['leftOp']): 
            return quad['result']
        return None 
    
    def gotoTrue(self, quad): 
        if self.virtualMemory.getValue(quad['leftOp']): 
            return quad['result']
        return None 
    
    def plusOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp + rightOp
        )
        return None 
    
    def minusOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp - rightOp
        )
    
    def multOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp * rightOp
        )
    
    def divOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp / rightOp
        )
    
    def equalOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp == rightOp
        )
    
    def andOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp and rightOp
        )
    
    def orOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp or rightOp
        )
    
    def notEqualOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp != rightOp
        )
    
    def greaterEqOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp >= rightOp
        )
    
    def lessEqOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp <= rightOp
        )
    
    def greaterOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp > rightOp
        )
    
    def lessOperator(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp < rightOp
        )
    
    def ver(self, quad): 
        arrayIndex = self.virtualMemory.getValue(quad['leftOp'])
        arrayILimit = self.virtualMemory.getValue(quad['rightOp'])
        arraySLimit = self.virtualMemory.getValue(quad['result'])

        if(arrayIndex < arrayILimit or arrayIndex >= arraySLimit): 
            print("Runtime Error: Array Index out of bounds.")
            sys.exit()

    def endProc(self, quad): 
        prevState = self.jumpStack.pop() + 1
        self.virtualMemory.restoreLocalMemory() 
        return prevState
    
    def era(self, quad): 
        self.virtualMemory.newLocalMemory() 
        return None 
    
    def param(self, quad): 
        self.virtualMemory.insertParameter(
            self.virtualMemory.getValue(quad['leftOp'])
        )
        return None 
    
    def gosub(self, quad): 
        self.virtualMemory.saveLocalMemory()
        self.virtualMemory.updateLocalMemory() 
        self.jumpStack.push(quad['QuadNo'])
        return quad['result']
    
    def returnVal(self, quad): 
        self.virtualMemory.updateMemory(
            quad['leftOp'], 
            self.virtualMemory.getValue(quad['result'])
        )
        return None 
    

