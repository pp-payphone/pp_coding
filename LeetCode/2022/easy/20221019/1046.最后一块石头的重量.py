#
# @lc app=leetcode.cn id=1046 lang=python3
#
# [1046] 最后一块石头的重量
#

# @lc code=start
class MaxHeap():
    def __init__(self):
        self._heap = []
        self.n = 0
        return
    
    def append(self, x):
        self._heap.append(x)
        self.n += 1
        self._up()
        return
    
    def _up(self):
        j = self.n - 1
        while j > 0:
            i = (j - 1) // 2
            if self._heap[i] >= self._heap[j]:
                break
            else:
                self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                j = i
        return
    
    def get_max(self):
        return self._heap[0]
    
    def pop(self):
        if self._heap == []:
            return None
        self._heap[0], self._heap[self.n - 1] = self._heap[self.n - 1], self._heap[0]
        max_v = self._heap.pop()
        self.n -= 1
        self._down()
        return max_v
    
    def _down(self):
        i = 0
        while i < self.n:
            j, k = i * 2 + 1, i * 2 + 2
            if j >= self.n:
                break
            elif k >= self.n:
                if self._heap[i] < self._heap[j]:
                    self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                    i = j
                break
            else:
                if self._heap[i] >= self._heap[j] and self._heap[i] > self._heap[k]:
                    break
                if self._heap[j] >= self._heap[k]:
                    self._heap[i], self._heap[j] = self._heap[j], self._heap[i]
                    i = j
                else:
                    self._heap[i], self._heap[k] = self._heap[k], self._heap[i]
                    i = k
        return


class Solution:
    # 最大堆，有意思
    def lastStoneWeight(self, stones) -> int:
        # stones.sort()
        # while len(stones) > 1:
        #     x, y = stones[-2], stones[-1]
        #     stones = stones[:-2]
        #     if x == y:
        #         continue
        #     else:
        #         new = y - x
        #     i = 0
        #     if stones == []:
        #         stones = [new]
        #         continue
        #     elif stones[-1] < new:
        #         stones.append(new)
        #         continue
        #     for i, w in enumerate(stones):
        #         if w >= new:
        #             break
        #     stones = stones[:i] + [new] + stones[i:]
        # if stones == []:
        #     return 0
        # else:
        #     return stones[0]

        max_hep = MaxHeap()
        for stone in stones:
            max_hep.append(stone)
        while max_hep.n > 1:
            x = max_hep.pop()
            y = max_hep.pop()
            if x > y:
                max_hep.append(x - y)
        res = max_hep.pop()
        if res is None:
            return 0
        else:
            return res

# @lc code=end

Solution().lastStoneWeight([2,4,1,4,1,7,3,8])