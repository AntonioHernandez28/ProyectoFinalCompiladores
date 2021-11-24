import sys
class Memory: 
    def __init__(self): 
        self.operators = {
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
            'VER' : 26, 
            'RETURN': 27,
            'sort' : 28 
        }
        
        self.COUNTERS = {
            'global' : {
                'int' : 1000, 
                'float' : 3000, 
                'char' : 5000,
            }, 
            'local' : {
                'int' : 9000, 
                'float' : 12000, 
                'char' : 15000
            }, 
            'temps' : {
                'int' : 18000, 
                'float' : 20000, 
                'char' : 22000, 
                'bool' : 25000,
            }, 
            'constants' : {
                'int' : 28000, 
                'float' : 30000, 
                'char' : 32000
            },
            'pointers' : {
                'int' : 37000, 
                'float': 39000, 
                'char' : 42000
            }
        }

        self.LIMITS = {
            'global' : {
                'int' : 3000, 
                'float' : 5000, 
                'char' : 7000,
            }, 
            'local' : {
                'int' : 12000, 
                'float' : 15000, 
                'char' : 18000
            }, 
            'temps' : {
                'int' : 20000, 
                'float' : 22000, 
                'char' : 25000, 
                'bool' : 27000
            }, 
            'constants' : {
                'int' : 30000, 
                'float' : 32000, 
                'char' : 34000
            }, 
            'pointers' : {
                'int' : 39000,
                'float' : 42000, 
                'char' : 45000
            }
        }

    def assignMemory(self, context, type):
        if self.COUNTERS[context][type] < self.LIMITS[context][type]: 
            self.COUNTERS[context][type] += 1 
            return self.COUNTERS[context][type]
        else: 
            print("No more space in memory :( ")
            sys.exit()

    
    def assignMemoryToArray(self, context, type, size): 
        print("Entro a asignart memoria a arreglo")
        if self.COUNTERS[context][type] < self.LIMITS[context][type]: 
            self.COUNTERS[context][type] += size 
        else: 
            print("No more space for array in memory.")

    
    def cleanLocalMemory(self): 
        self.COUNTERS['local']['int'] = 9000
        self.COUNTERS['local']['float'] = 12000
        self.COUNTERS['local']['char'] = 15000
        self.COUNTERS['temps']['int'] = 18000
        self.COUNTERS['temps']['float'] = 20000
        self.COUNTERS['temps']['char'] = 22000
        self.COUNTERS['temps']['bool'] = 25000
    
    def getOperatorCode(self, operator): 
        return self.operators[operator]
    


            







        


