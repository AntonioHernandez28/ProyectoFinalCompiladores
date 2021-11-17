class Memory: 
    def __init__(self): 
    
        self.Globals = {}
        self.Locals = {}
        self.Temporals = {}
        self.Constants = {}

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
            'GotoV' : 25
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
                'bool' : 25000
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
            }
        }

    def assignMemory(self, context, type):
        if self.COUNTERS[context][type] < self.LIMITS[context][type]: 
            self.COUNTERS[context][type] += 1 
            return self.COUNTERS[context][type]
    
    def cleanLocalMemory(self): 
        self.COUNTERS['local']['int'] = 9000
        self.COUNTERS['local']['float'] = 12000
        self.COUNTERS['local']['char'] = 15000
        self.COUNTERS['temps']['int'] = 18000
        self.COUNTERS['temps']['float'] = 20000
        self.COUNTERS['temps']['char'] = 22000
        self.COUNTERS['temps']['bool'] = 25000
        self.Temporals = {}
    
    def getOperatorCode(self, operator): 
        return self.operators[operator]
    


            







        


