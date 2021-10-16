import sys 

class VariablesTable: 

    def __int__(self): 
        self.variablesList = { } # Start Dictionary 

    def add(self, id, type): 
        self.variablesList[id] = { # Nested dictionary to add more attributes if needed in future. 
            'type' : type 
        }
    
    def searchVariable(self, id): 
        return id in self.variablesList
    
    def printVariable(self): 
        for i in self.variablesList: 
            print(i, ' Variable in List ')
    
