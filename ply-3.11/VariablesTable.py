import sys 

class VariablesTable: 

    def __init__(self):
        self.variablesList = { }

    def add(self, id, type): 
        self.variablesList[id] = { # Nested dictionary to add more attributes if needed in future. 
            'type' : type 
        }
    
    def searchVariable(self, id): 
        return id in self.variablesList.keys()

    def getType(self, id): 
        return self.variablesList[id]['type']
    
    def printVariable(self): 
        for i in self.variablesList: 
            print(i, ' Variable in List ')
    

class Var(): 
    def __init__(self, type, id): 
        self.type = type 
        self.id = id 
