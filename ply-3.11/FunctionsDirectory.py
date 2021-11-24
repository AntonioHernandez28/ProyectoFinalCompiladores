from VariablesTable import VariablesTable 
import sys 

#Functions Directory  
class FunctionsDirectory(): 

    def __init__ (self): 
        self.funcDirectory = {} 
    
    def addFunction(self, type, funcID, numberParams, typeParams, nameParams, startDirection, numberVars, totalSize): 
        if funcID not in self.funcDirectory.keys(): # Check if function do not exist in function directory yet 
            self.funcDirectory[funcID] = {
                'type' : type, 
                'numberParams' : numberParams, 
                'typeParams' : typeParams, 
                'nameParams' : nameParams, 
                'localVariables' : VariablesTable(), 
                'startDirection' : startDirection,
                'numberVars' : numberVars,  # VariablesTable.size()? 
                'totalSize' : totalSize
            }
            print("Function successfuly added: ", funcID, ' ', type)
        
        else: 
            print("Error, function already exists in Directory: ", funcID)
            sys.exit()
        
    
    def getSizeForArray(self, funcID, varID): 
        if self.funcDirectory['program']['localVariables'].searchVariable(varID):
            return self.funcDirectory['program']['localVariables'].getSizeArray(varID)
        elif self.funcDirectory[funcID]['localVariables'].searchVariable(varID):
            return self.funcDirectory[funcID]['localVariables'].getSizeArray(varID)
        else:
            print("Variable has not been declared.")
            sys.exit()

    def setSizeForArray(self, funcID, varID, size): 
        if self.funcDirectory['program']['localVariables'].searchVariable(varID):
            return self.funcDirectory['program']['localVariables'].setSizeArray(varID, size)
        elif self.funcDirectory[funcID]['localVariables'].searchVariable(varID):
            return self.funcDirectory[funcID]['localVariables'].setSizeArray(varID, size)

    
    def getNumberVars(self, funcID): 
        return self.funcDirectory[funcID]['localVariables'].getSize() 
    
    def setTotalSize(self, funcID, size): 
        self.funcDirectory[funcID]['totalSize'] = size 

    def setStartDir(self, funcID, direction): 
        self.funcDirectory[funcID]['startDirection'] = direction
    
    def getDirection(self, funcID): 
        return self.funcDirectory[funcID]['startDirection']

    def searchFunction(self, id): 
        return id in self.funcDirectory
    
    def addVariable(self, funcID, type, currentId, currentAddress): 
        if self.funcDirectory[funcID]['localVariables'].searchVariable(currentId) or self.funcDirectory['program']['localVariables'].searchVariable(currentId): 
            print("This variable already exists for this function: ", currentId)
        else: 
            self.funcDirectory[funcID]['localVariables'].add(currentId, type, currentAddress) 
            print("Variable successfully added to function's local variables: ", currentId, " of type: ", type, " -> ",funcID)
    
    def printFunctionVariables(self, funcID): 
        if funcID in self.funcDirectory: 
            self.funcDirectory[funcID]['localVariables'].printVariable()
    
    def searchVariable(self, funcID, varID):
        if self.funcDirectory[funcID]['localVariables'].searchVariable(varID) or self.funcDirectory['program']['localVariables'].searchVariable(varID): 
            return True 
        else: 
            print("Var: ", varID, " does NOT exist in Scope: ", funcID)

    def getVarType(self, funcID, varID): 
        if self.funcDirectory[funcID]['localVariables'].searchVariable(varID):
            return self.funcDirectory[funcID]['localVariables'].getType(varID)
        elif self.funcDirectory['program']['localVariables'].searchVariable(varID): 
            return self.funcDirectory['program']['localVariables'].getType(varID)
        else: 
            print("Variable: ", varID, " does NOT exist in Scope: ", funcID)
        
    def getNumberParameters(self, funcID): 
        return self.funcDirectory[funcID]['numberParams']

    def addParameters(self, funcID, funcName, funcType): 
        self.funcDirectory[funcID]['numberParams'] += 1 
        self.funcDirectory[funcID]['nameParams'].append(funcName)
        self.funcDirectory[funcID]['typeParams'].append(funcType)
    
    def getParamsTypes(self, funcID): 
        return self.funcDirectory[funcID]['typeParams']
    
    def getParamsNames(self, funcID): 
        return self.funcDirectory[funcID]['nameParams']
    
    def getDirectionById(self, funcID, varID): 
        if self.searchVariable('program', varID): 
            return self.funcDirectory['program']['localVariables'].getAddress(varID)
        elif(self.searchVariable(funcID, varID)): 
            return self.funcDirectory[funcID]['localVariables'].getAddress(varID)
        else: 
            print("Variable not declared yet.")
        
    def getFunctionType(self, funcID): 
        if funcID in self.funcDirectory: 
            return self.funcDirectory[funcID]['type']
    
    def getGlobalVar(self, varID): 
        if self.funcDirectory['program']['localVariables'].searchVariable(varID):
            return self.funcDirectory['program']['localVariables'].getAddress(varID)
    

    def printFunction(self, funcID): 
        print("ID: ", funcID)
        print("Type: ", self.funcDirectory[funcID]['type'])
        print("Number Of Params: ", self.funcDirectory[funcID]['numberParams'])
        print("Type Of Params: ")
        print(self.funcDirectory[funcID]['typeParams'])
        print("Name Of Params: ")
        print(self.funcDirectory[funcID]['nameParams'])
        print("Name Of Variables: ")
        self.printFunctionVariables(funcID)
        print("Number Of Variables: ", self.funcDirectory[funcID]['numberVars'])
