# https://leetcode-cn.com/problems/lru-cache/

class LRUCache(collections.OrderedDict):

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if not key in self:
            return -1
        else:
            self.move_to_end(key)
            return self[key]
        
    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self[key] = value
        while self.__len__() > self.capacity:
            self.popitem(0)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)