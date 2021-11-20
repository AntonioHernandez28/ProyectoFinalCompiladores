class Quadruples: 
    def __init__(self):
        self.quadruples = [] 
    
    def addQuad(self, operator, leftOp, rightOp, result): 
        self.quadruples.append({
            'QuadNo' : len(self.quadruples),
            'operator' : operator, 
            'leftOp' : leftOp, 
            'rightOp' : rightOp, 
            'result' : result
        })
    
    def updateQuad(self, operator, leftOp, rightOp, result, address): 
        self.quadruples[address] = {
            'QuadNo' : self.quadruples[address]['QuadNo'], 
            'operator' : operator, 
            'leftOp' : leftOp, 
            'rightOp' : rightOp, 
            'result' : result
        }
    
    def displayQuads(self): 
       for quadruple in self.quadruples:
            print(str(quadruple["QuadNo"]) 
                + '\t' + str(quadruple["operator"])
                + '\t' + str(quadruple["leftOp"])
                + '\t' + str(quadruple["rightOp"])
                + '\t' + str(quadruple["result"]))
