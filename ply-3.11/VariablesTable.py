import sys 

class VariablesTable: 

    def __init__(self):
        self.variablesList = { }

    def add(self, id, type, virAddress): 
        self.variablesList[id] = { # Nested dictionary to add more attributes if needed in future. 
            'type' : type, 
            'address': virAddress, 
            'dim' : 0
        }
        print("Se asigno memoria a: ", id, " que fue la: ", virAddress)
    
    def getAddress(self, id): 
        print("Si esta buscando en el ID: ", id)
        return self.variablesList[id]['address'] 
    
    def searchVariable(self, id): 
        return id in self.variablesList.keys()

    def getType(self, id): 
        return self.variablesList[id]['type']
    
    def printVariable(self): 
        for i in self.variablesList: 
            print("Variable: ", i, " with address: ", self.variablesList[i]['address'])
    
    def getSize(self): 
        return len(self.variablesList)
    
    def setSizeArray(self, id, size):
        self.variablesList[id]['dim'] = size

    
    def getSizeArray(self, id): 
        print("ID en getSizeArray es: ", id)
        if not id in self.variablesList: 
            print("Var has not been declared in this scope") 
            return None 
        if self.variablesList[id]['dim'] == 0: 
            print("This variable is NOT an array.")
            sys.exit()
            return None 
        else: 
            return self.variablesList[id]['dim']

class Var(): 
    def __init__(self, type, id): 
        self.type = type 
        self.id = id 
