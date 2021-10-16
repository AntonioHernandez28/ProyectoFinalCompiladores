from VariablesTable import VariablesTable 
import sys 

#Functions Directory  
class FunctionsDirectory(): 

    def __init__ (self): 
        self.funcDirectory = {} 
    
    def addFunction(self, type, funcID, numberParams, typeParams, nameParams, numberVars): 
        if funcID not in self.funcDirectory.keys(): # Check if function do not exist in function directory yet 
            self.funcDirectory[funcID] = {
                'type' : type, 
                'numberParams' : numberParams, 
                'typeParams' : typeParams, 
                'nameParams' : nameParams, 
                'localVariables' : VariablesTable(), 
                'numberVars' : numberVars # VariablesTable.size()? 
            }
            print("Function successfuly added: ", funcID, ' ', type)
        
        else: 
            print("Error, function already exists in Directory: ", funcID)

    
    def searchFunction(self, id): 
        return id in self.funcDirectory
    
    def addVariable(self, funcID, type, currentId): 
        if(self.funcDirectory[funcID]['localVariables'].searchVariable(currentId)): 
            print("This variable already exists for this function.", currentId)
        else: 
            self.funcDirectory[funcID]['localVariables'].add(currentId, type) 
            print("Variable successfully added to function's local variables. ", funcID)
    
    def printFunctionVariables(self, funcID): 
        if funcID in self.funcDirectory: 
            self.funcDirectory[funcID]['localVariables'].printVariable()
    
    def printFunction(self, funcID): 
        print("ID: " + funcID)
        print("Type: " + self.funcDirectory[funcID]['type'])
        print("Number Of Params: " + self.funcDirectory[funcID]['numberParams'])
        print("Type Of Params: ")
        print(self.funcDirectory[funcID]['typeParams'])
        print("Name Of Params: ")
        print(self.funcDirectory[funcID]['nameParams'])
        print("Name Of Variables: ")
        self.printFunctionVariables(funcID)
        print("Number Of Variables: " + self.funcDirectory[funcID]['numberVars'])
