def simple_hash(key):
    key = str(key)
    code = ord(key[0])
    return code % 20

class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = simple_hash(key)
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = simple_hash(key)
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)
            
class HashTable():
    
    def __init__(self, size):
        self.array = np.zeros(size, dtype=np.object)
        self.size = size
    
    def __getitem__(self, key):
        ind = hash(key) % self.size
        for k,v in self.array[ind]:
            if key == k:
                return v
    
    def __setitem__(self, key, value):
        ind = hash(key) % self.size
        if not isinstance(self.array[ind], list):
            self.array[ind] = []
        replace = None
        for i,data in enumerate(self.array[ind]):
            if data[0] == key:
                replace = i
        if replace is None:
            self.array[ind].append((key,value))
        else:
            self.array[ind][replace] = (key, value)