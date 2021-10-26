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
            12: '|',
            13: '=',
            14: '=='
            }
            
        self.types = {
            1: 'int',
            2: 'float',
            3: 'char',
            4: 'bool',
            5: 'CTEI',
            6: 'CTEF',
            7: 'CTEC',
            8: 'CTESTRING',
            9: 'ERROR',
            }


        self.compatibility = {
            # int
            self.types[1]: {
                # int-int compatibility
                self.types[1]: {
                    self.operators[1]: self.types[1],
                    self.operators[2]: self.types[1],
                    self.operators[3]: self.types[1],
                    self.operators[4]: self.types[1],
                    self.operators[5]: self.types[4],
                    self.operators[6]: self.types[4],
                    self.operators[7]: self.types[4],
                    self.operators[8]: self.types[4],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[1],
                    self.operators[14]: self.types[4],
                },
                # int-float compatibility
                self.types[2]: {
                    self.operators[1]: self.types[2],
                    self.operators[2]: self.types[2],
                    self.operators[3]: self.types[2],
                    self.operators[4]: self.types[2],
                    self.operators[5]: self.types[4],
                    self.operators[6]: self.types[4],
                    self.operators[7]: self.types[4],
                    self.operators[8]: self.types[4],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # int-char compatibility
                self.types[3]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                 #int-bool compatibility
                self.types[4]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },

            },
            # float
            self.types[2]: {
                    # float-int compatibility
                self.types[1]: {
                    self.operators[1]: self.types[2],
                    self.operators[2]: self.types[2],
                    self.operators[3]: self.types[2],
                    self.operators[4]: self.types[2],
                    self.operators[5]: self.types[4],
                    self.operators[6]: self.types[4],
                    self.operators[7]: self.types[4],
                    self.operators[8]: self.types[4],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],

                },
                # float-float compatibility
                self.types[2]: {
                    self.operators[1]: self.types[2],
                    self.operators[2]: self.types[2],
                    self.operators[3]: self.types[2],
                    self.operators[4]: self.types[2],
                    self.operators[5]: self.types[4],
                    self.operators[6]: self.types[4],
                    self.operators[7]: self.types[4],
                    self.operators[8]: self.types[4],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[2],
                    self.operators[14]: self.types[4],
                },
                # float-char compatibility
                self.types[3]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                 #bool-float compatibility
                self.types[4]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
            },
            # char
            self.types[3]: {
                    # char-int compatibility
                self.types[1]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # char-float compatibility
                self.types[2]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # char-char compatibility
                self.types[3]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[3],
                    self.operators[14]: self.types[4],
                },
                 #char-bool compatibility
                self.types[4]:{
                    self.operators[1]:self.types[9],
                    self.operators[2]:self.types[9],
                    self.operators[3]:self.types[9],
                    self.operators[4]:self.types[9],
                    self.operators[5]:self.types[9],
                    self.operators[6]:self.types[9],
                    self.operators[7]:self.types[9],
                    self.operators[8]:self.types[9],
                    self.operators[9]:self.types[9],
                    self.operators[10]:self.types[9],
                    self.operators[11]:self.types[9],
                    self.operators[12]:self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },

            },
            # BOOLEAN
            self.types[4]: {
                # bool-int COMPAT
                self.types[1]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # bool-float compatibility
                self.types[2]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # bool-char compatibility
                self.types[3]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[9],
                    self.operators[6]: self.types[9],
                    self.operators[7]: self.types[9],
                    self.operators[8]: self.types[9],
                    self.operators[9]: self.types[9],
                    self.operators[10]: self.types[9],
                    self.operators[11]: self.types[9],
                    self.operators[12]: self.types[9],
                    self.operators[13]: self.types[9],
                    self.operators[14]: self.types[9],
                },
                # bool bool compatibility
                self.types[4]: {
                    self.operators[1]: self.types[9],
                    self.operators[2]: self.types[9],
                    self.operators[3]: self.types[9],
                    self.operators[4]: self.types[9],
                    self.operators[5]: self.types[4],
                    self.operators[6]: self.types[4],
                    self.operators[7]: self.types[4],
                    self.operators[8]: self.types[4],
                    self.operators[9]: self.types[4],
                    self.operators[10]: self.types[4],
                    self.operators[11]: self.types[4],
                    self.operators[12]: self.types[4],
                    self.operators[13]: self.types[4],
                    self.operators[14]: self.types[4],
                },
            },

        }
    
    # Semantic Cube implemented for getting type 
    def getType(self, left, right, operator): 
        return self.compatibility[left][right][operator]

    # Print Type Expected 
    def printExpected(self, left, right, operator): 
        print("Expected type for provided types and operator is: " + self.getType(left, right, operator))


