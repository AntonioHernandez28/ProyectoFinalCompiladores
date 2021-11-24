from VirtualMemory import VirtualMemory
from stack import Stack
import numpy as np 
import matplotlib.pyplot as plt
from statistics import mode, variance
import json 
import sys 

class OperationHandler: 
    def __init__(self): 
        self.virtualMemory = VirtualMemory()
        self.jumpStack = Stack() 
    
    def loadConstantTable(self, constants): 
        for i in constants: 
            currentConstant = json.loads(i)
            print(str(currentConstant['constant']))
            print(str(currentConstant['address']))
            self.virtualMemory.updateMemory(
                currentConstant['address'],
                currentConstant['constant']
            )
        
    def assign(self, quad): 
        print("Entro al assign")
        leftOp = quad['leftOp']
        result = quad['result']
        if self.virtualMemory.checkIfPointer(result):
            result = self.virtualMemory.getPointerValue(result)
        self.virtualMemory.updateMemory(
            result, 
            self.virtualMemory.getValue(leftOp)
        )
    
    def write(self, quad): 
        print("WRITE QUAD -> ", quad)
        value = self.virtualMemory.getValue(
            quad['result']
        )
        print("Compiler writes: ", value)
    
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
        if self.virtualMemory.checkIfPointer(result): 
            result = self.virtualMemory.getPointerValue(result)
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
        print("PLUS QUAD: ", str(quad))
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        print("Se trajo de get value el lefrOP: ", leftOp)
        print("Se trajo de get value el rightOp que DEBE de ser la const con la base dir: ", rightOp)
        self.virtualMemory.updateMemory(
            quad['result'], 
            leftOp + rightOp
        )
        #print("Se guardo: ", leftOp + rightOp, " en la dir: ", quad['result'], ", funciono? ", self.virtualMemory.getValue(quad['result']))
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
        print("Param Quad: ", str(quad))
        self.virtualMemory.insertParameter(
            self.virtualMemory.getValue(quad['rightOp'])
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
    
    def ver(self, quad): 
        leftOp = self.virtualMemory.getValue(quad['leftOp'])
        rightOp = self.virtualMemory.getValue(quad['rightOp'])
        result = self.virtualMemory.getValue(quad['result'])
        if not (leftOp >= rightOp and leftOp < result): 
            print("Index Array out of bounds.")
            sys.exit()
        return None 
    
    def sort(self, quad): 
        startValue = quad['leftOp']
        length = quad['result']
        currArray = []
        startDirection = startValue
        endDirection = startValue + length

        while(startDirection < endDirection): 
            currArray.append(
                self.virtualMemory.getValue(startDirection)
            )
            startDirection += 1
        
        startDirection = startValue
        currArray.sort() 
        while (startDirection < endDirection): 
            self.virtualMemory.updateMemory(
                startDirection, 
                currArray.pop(0)
            )
            startDirection += 1 
            
        return None 

    def mean(self, quad): 
        startValue = quad['leftOp']
        direction = quad['rightOp']
        length = quad['result']
        currArray = []
        startDirection = startValue
        endDirection = startValue + length

        while(startDirection < endDirection): 
            currArray.append(
                self.virtualMemory.getValue(startDirection)
            )
            startDirection += 1
        value = np.mean(currArray)
        self.virtualMemory.updateMemory(
            direction, 
            value
        )
    
    def find(self, quad): 
        startValue = quad['leftOp']['startDirection']
        valueToFind = self.virtualMemory.getValue(quad['leftOp']['valueToFind'])
        direction = quad['rightOp']
        length = quad['result']
        currArray = []
        startDirection = startValue 
        endDirection = startValue + length

        while(startDirection < endDirection): 
            currArray.append(
                self.virtualMemory.getValue(startDirection)
            )
            startDirection += 1
        
        indexResult = -1 
        counter = 0 
        print("EN VM el valor a buscar es: ", valueToFind)
        for i in currArray: 
            if i == valueToFind: 
                indexResult = counter 
                break
            counter += 1 
        
        self.virtualMemory.updateMemory(
            direction, 
            indexResult
        )
    
    def mode(self, quad): 
        startValue = quad['leftOp']
        direction = quad['rightOp']
        length = quad['result']
        currArray = []
        startDirection = startValue
        endDirection = startValue + length

        while(startDirection < endDirection): 
            currArray.append(
                self.virtualMemory.getValue(startDirection)
            )
            startDirection += 1
        value = mode(currArray)
        self.virtualMemory.updateMemory(
            direction, 
            value
        )
    
    def variance(self, quad): 
        startValue = quad['leftOp']
        direction = quad['rightOp']
        length = quad['result']
        currArray = []
        startDirection = startValue
        endDirection = startValue + length

        while(startDirection < endDirection): 
            currArray.append(
                self.virtualMemory.getValue(startDirection)
            )
            startDirection += 1
        value = variance(currArray)
        self.virtualMemory.updateMemory(
            direction, 
            value
        )

    def plot(self, quad): 
        startValueArr1 = quad['leftOp']
        startValueArr2 = quad['rightOp']
        lengthArr1 = quad['result']['SizeArray1']
        length1Arr2 = quad['result']['SizeArray2']
        currArrayX = []
        currArrayY = []
        startDirectionX = startValueArr1
        endDirectionX = startValueArr1 + lengthArr1

        startDirectionY = startValueArr2
        endDirectionY = startValueArr2 + length1Arr2


        while(startDirectionX < endDirectionX): 
            currArrayX.append(
                self.virtualMemory.getValue(startDirectionX)
            )
            startDirectionX += 1
        
        while(startDirectionY < endDirectionY): 
            currArrayY.append(
                self.virtualMemory.getValue(startDirectionY)
            )
            startDirectionY += 1
        
        plt.scatter(currArrayX, currArrayY)
        plt.show()

        return None 




    

    

