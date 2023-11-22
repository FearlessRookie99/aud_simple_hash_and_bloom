
# BloomFilter als Klasse definieren 
class BloomFilter:
    def __init__(self, size, hash_funcs):
        self.size = size
        self.array = [False] * size
        self.hash_funcs = hash_funcs

    # codiert ein neues Element im Bloom Filter
    def insert(self, element):
        for func in self.hash_funcs:
            index = func(element) % self.size
            self.array[index] = True
            
    # sucht nach einem Element im Bloom Filter 
    def search(self, element):
        for func in self.hash_funcs:
            index = func(element) % self.size
            if not self.array[index]:
                return False
        return True

