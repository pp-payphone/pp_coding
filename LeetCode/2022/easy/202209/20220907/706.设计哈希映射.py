#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] 设计哈希映射
#

# @lc code=start
class MyHashMap:
    def __init__(self):
        self.N = 1009        
        self.data = [[] for _ in range(self.N)]

    def getHashKey(self, key):
        return key % self.N

    def put(self, key, value):
        hashKey = self.getHashKey(key)
        for entry in self.data[hashKey]:
            if entry[0] == key:
                entry[1] = value
                return
        self.data[hashKey].append([key, value])

    def get(self, key):
        hashKey = self.getHashKey(key)
        for entry in self.data[hashKey]:
            if entry[0] == key:
                return entry[1]
        return -1

    def remove(self, key):
        hashKey = self.getHashKey(key);
        for index, entry in enumerate(self.data[hashKey]):
            if entry[0] == key:
                self.data[hashKey].pop(index)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

