class Avail(object): 
    def __init__(self): 
        self.avail = 0 
        self.tmem = 'T'

    def next(self): 
        self.avail += 1
        return self.tmem + str(self.avail)
    
    def clear(self): 
        self.avail = 0 