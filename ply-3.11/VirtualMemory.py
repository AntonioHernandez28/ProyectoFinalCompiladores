import sys 
class VirtualMemory:
    def __init__(self): 
        self.memory = {
            'global' : {}, 
            'constant' : {},
            'local' : {},
            'temporal' : {}, 
            'pointers' : {}
        }

        self.BOUNDARIES = {
            'global_iLimit' : 1000, 
            'global_sLimit' : 8999, 
            'local_iLimit' : 9001, 
            'local_sLimit' : 17999, 
            'temporal_iLimit' : 18000, 
            'temporal_sLimit' : 27999, 
            'constant_iLimit' : 28000,
            'constant_sLimit' : 36999, 
            'pointer_iLimit' : 37000, 
            'pointer_sLimit' : 44999
        }

        self.new_local_mem_cache = {}
        self.localCounter = self.BOUNDARIES['local_iLimit'] 
        self.memorySnapshots = {
            'temporal' : [], 
            'local' : []
        }

    def updateAddress(self, virtualAddress, context, value): 
        #print("Entro a guardar la hdp address: ", virtualAddress, " value: ", value)
        self.memory[context][virtualAddress] = value
        #print("checalo we: ", self.getValue(virtualAddress))
    
    def checkValueInMemory(self, virtualAddress, context): 
        if virtualAddress in self.memory[context]: 
            return self.memory[context][virtualAddress]
        else: 
            print("Address: ", virtualAddress, " has NOT been initialized.")
            sys.exit()
            return None 
    
    def newLocalMemory(self): 
        self.new_local_mem_cache = {}
        self.localCounter = self.BOUNDARIES['local_iLimit']
    
    def insertParameter(self, value): 
        #print("Param inserted in address: ", self.localCounter)
        self.new_local_mem_cache[self.localCounter] = value 
        self.localCounter += 1
    
    def saveLocalMemory(self): 
        self.memorySnapshots['local'].append(
            self.memory['local']
        )
        self.memorySnapshots['temporal'].append(
            self.memory['temporal']
        )
    
    def restoreLocalMemory(self): 
        self.memory['local'] = self.memorySnapshots['local'].pop() 
        self.memory['temporal'] = self.memorySnapshots['temporal'].pop() 
    
    def updateLocalMemory(self): 
        self.memory['local'] = self.new_local_mem_cache
        self.memory['temporal'] = {}
    
    def checkIfPointer(self, address): 
        if (address >= self.BOUNDARIES['pointer_iLimit'] and address <= self.BOUNDARIES['pointer_sLimit']):
            return True 
        return False 
    
    def getPointerValue(self, address): 
        return self.checkValueInMemory(address, 'pointers')
    
    def getValue(self, address): 
        #print("ADRESS IN GET VALUE: ", address)
        if (address >= self.BOUNDARIES['global_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.checkValueInMemory(address, 'global')
        if (address >= self.BOUNDARIES['local_iLimit'] and address <= self.BOUNDARIES['local_sLimit']): #Local Memory
            return self.checkValueInMemory(address, 'local')
        if (address >= self.BOUNDARIES['temporal_iLimit'] and address <= self.BOUNDARIES['temporal_sLimit']): #Temporal Memory
            return self.checkValueInMemory(address, 'temporal')
        if (address >= self.BOUNDARIES['constant_iLimit'] and address <= self.BOUNDARIES['constant_sLimit']): #Constant Memory
            return self.checkValueInMemory(address, 'constant')
        if (address >= self.BOUNDARIES['pointer_iLimit'] and address <= self.BOUNDARIES['pointer_sLimit']): #Pointer Memory
            return self.getValue(self.checkValueInMemory(address, 'pointers'))
        
    
    def updateMemory(self, address, value): 
        #print("Entro a memoria: ", address, " valor: ", value)
        if (address >= self.BOUNDARIES['global_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.updateAddress(address, 'global', value)
        if (address >= self.BOUNDARIES['local_iLimit'] and address <= self.BOUNDARIES['local_sLimit']): #Global Memory
            return self.updateAddress(address, 'local', value)
        if (address >= self.BOUNDARIES['temporal_iLimit'] and address <= self.BOUNDARIES['temporal_sLimit']): #Global Memory
            return self.updateAddress(address, 'temporal', value)
        if (address >= self.BOUNDARIES['constant_iLimit'] and address <= self.BOUNDARIES['constant_sLimit']): #Global Memory
            return self.updateAddress(address, 'constant', value)
        if (address >= self.BOUNDARIES['pointer_iLimit'] and address <= self.BOUNDARIES['pointer_sLimit']): #Global Memory
            return self.updateAddress(address, 'pointers', value)
    




