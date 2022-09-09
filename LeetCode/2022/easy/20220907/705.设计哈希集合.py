#
# @lc app=leetcode.cn id=705 lang=python3
#
# [705] 设计哈希集合
#

# @lc code=start
# 理论上都应该再O(1)复杂度下完成，这个真是让人没有思路
class MyHashSet:

    def __init__(self):
        self._a = [False for _ in range(10 ** 6 + 1)]

    def add(self, key: int) -> None:
        self._a[key] = True

    def remove(self, key: int) -> None:
        self._a[key] = False

    def contains(self, key: int) -> bool:
        return self._a[key]



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end

