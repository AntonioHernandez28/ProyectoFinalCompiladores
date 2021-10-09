class SemanticCube: 

    def __init__(self): 
        # Operators used in the language 
        self.operators = {
            1: '+',
            2: '-',
            3: '*',
            4: '/',
            5: '<',
            6: '>',
            7: '<=',
            8: '>=',
            9: '==',
            10: '!=',
            11: '&&',
            12: '|'
        }

        self.types = {
            1: 'int',
            2: 'float',
            3: 'char',
            4: 'bool',
            5: 'CTEI', # Constants
            6: 'CTEF', # Constants
            7: 'CTEC', # Constants 
            8: 'CTESTRING',
            9: 'ERROR',
        }

        self.compability = {
            # INTEGER 
            self.types[1]: {
                # INT - INT compability 
                self.types[1]: {
                    self.operators[1] : self.types[1], 
                    self.operators[2] : self.types[1], 
                    self.operators[3] : self.types[1], 
                    self.operators[4] : self.types[1], 
                    self.operators[6] : self.types[4],
                    self.operators[7] : self.types[4],
                    self.operators[8] : self.types[4],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },
                
                # INT - FLOAT compatibility 
                self.types[2]: {
                    self.operators[1] : self.types[2],
                    self.operators[2] : self.types[2],
                    self.operators[3] : self.types[2],
                    self.operators[4] : self.types[2],
                    self.operators[5] : self.types[4],
                    self.operators[6] : self.types[4],
                    self.operators[7] : self.types[4],
                    self.operators[8] : self.types[4],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[4],
                    self.operators[12] : self.types[4],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                }, 

                # INT - CHAR compatibility 
                 self.types[3]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },

                # INT - BOOL compability 
                 self.types[4]:{
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                    
                },


            }, 
            # FLOAT 
             self.types[2]: {

                    # FLOAT - INT compatibility
                self.types[1]: {
                    self.operators[1] : self.types[2],
                    self.operators[2] : self.types[2],
                    self.operators[3] : self.types[2],
                    self.operators[4] : self.types[2],
                    self.operators[5] : self.types[4],
                    self.operators[6] : self.types[4],
                    self.operators[7] : self.types[4],
                    self.operators[8] : self.types[4],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],

                },

                # FLOAT - FLOAT compatibility
                self.types[2]: {
                    self.operators[1] : self.types[2],
                    self.operators[2] : self.types[2],
                    self.operators[3] : self.types[2],
                    self.operators[4] : self.types[2],
                    self.operators[5] : self.types[4],
                    self.operators[6] : self.types[4],
                    self.operators[7] : self.types[4],
                    self.operators[8] : self.types[4],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],

                },

                # FLOAT - CHAR  compatibility
                self.types[3]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },

                 # BOOL - FLOAT compatibility
                self.types[4]:{
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                    
                },
            },

            # CHAR 
            self.types[3]: {

                # CHAR - INT compatibility 
                self.types[1]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },

                # CHAR - FLOAT compatibility
                self.types[2]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],

                },

                # CHAR - CHAR compatibility
                self.types[3]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },

                 # CHAR - BOOL compatibility
                self.types[4]:{
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                    
                },

            },

             # BOOLEAN
            self.types[4]: {

                # BOOL - INT compatibility
                self.types[1]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],

                },

                # BOOL - FLOAT compatibility
                self.types[2]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],

                },

                # BOOL - CHAR compatibility
                self.types[3]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[9],
                    self.operators[6] : self.types[9],
                    self.operators[7] : self.types[9],
                    self.operators[8] : self.types[9],
                    self.operators[9] : self.types[9],
                    self.operators[10] : self.types[9],
                    self.operators[11] : self.types[9],
                    self.operators[12] : self.types[9],
                },

                # BOOL - BOOL compatibility
                self.types[4]: {
                    self.operators[1] : self.types[9],
                    self.operators[2] : self.types[9],
                    self.operators[3] : self.types[9],
                    self.operators[4] : self.types[9],
                    self.operators[5] : self.types[4],
                    self.operators[6] : self.types[4],
                    self.operators[7] : self.types[4],
                    self.operators[8] : self.types[4],
                    self.operators[9] : self.types[4],
                    self.operators[10] : self.types[4],
                    self.operators[11] : self.types[4],
                    self.operators[12] : self.types[4],
                },
            },
        }
    
    # Semantic Cube implemented for getting type 
    def getType(self, left, right, operator): 
        return self.compability[left][right][operator]

    # Print Type Expected 
    def printExpected(self, left, right, operator): 
        print("Expected type for provided types and operator is: " + self.getType(left, right, operator))


