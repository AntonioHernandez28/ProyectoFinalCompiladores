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
            'local_iLimit' : 9000, 
            'local_sLimit' : 17999, 
            'temporal_iLimit' : 18000, 
            'temporal_sLimit' : 27999, 
            'constant_iLimit' : 28000,
            'constant_sLimit' : 36999
        }

        self.new_local_mem_cache = {}
        self.localCounter = self.BOUNDARIES['local_iLimit']
        self.memorySnapshots = {
            'temporal' : [], 
            'local' : []
        }

    def updateAddress(self, virtualAddress, context, value): 
        self.memory[context][virtualAddress] = value
    
    def checkValueInMemory(self, virtualAddress, context): 
        if virtualAddress in self.memory[context]: 
            return self.memory[context][virtualAddress]
        else: 
            print("Address not registered in memory.")
            return None 
    
    def newLocalMemory(self): 
        self.new_local_mem_cache = {}
        self.localCounter = self.BOUNDARIES['local_iLimit']
    
    def insertParameter(self, value): 
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
    
    def getValue(self, address): 
        if (address >= self.BOUNDARIES['global_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.checkValueInMemory(address, 'global')
        if (address >= self.BOUNDARIES['local_iLimit'] and address <= self.BOUNDARIES['local_sLimit']): #Global Memory
            return self.checkValueInMemory(address, 'local')
        if (address >= self.BOUNDARIES['temporal_iLimit'] and address <= self.BOUNDARIES['temporal_sLimit']): #Global Memory
            return self.checkValueInMemory(address, 'temporal')
        if (address >= self.BOUNDARIES['constant_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.checkValueInMemory(address, 'constant')
    
    def updateMemory(self, address): 
        if (address >= self.BOUNDARIES['global_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.updateMemory(address, 'global')
        if (address >= self.BOUNDARIES['local_iLimit'] and address <= self.BOUNDARIES['local_sLimit']): #Global Memory
            return self.updateMemory(address, 'local')
        if (address >= self.BOUNDARIES['temporal_iLimit'] and address <= self.BOUNDARIES['temporal_sLimit']): #Global Memory
            return self.updateMemory(address, 'temporal')
        if (address >= self.BOUNDARIES['constant_iLimit'] and address <= self.BOUNDARIES['global_sLimit']): #Global Memory
            return self.updateMemory(address, 'constant')
    




