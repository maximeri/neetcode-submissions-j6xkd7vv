class LRUCache:
    # Brute force
    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                tmp = self.cache.pop(i)
                self.cache.append(tmp)
                return tmp[1]
        return -1
        

    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
             if self.cache[i][0] == key:
                self.cache.pop(i)
                break

        self.cache.append([key, value])
        if len(self.cache) > self.capacity:
            self.cache.pop(0)

