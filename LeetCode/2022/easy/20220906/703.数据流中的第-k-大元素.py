#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第 K 大元素
#

# @lc code=start
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.append(-99999)
        nums.sort(reverse=False)
        self.nums = nums[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if val <= self.nums[0]:
            return self.nums[0]
        elif self.k == 1:
            self.nums = [val]
            return val
        else:
            self.nums[0] = val
            for i in range(1, self.k):
                if val > self.nums[i]:
                    self.nums[i - 1], self.nums[i] = self.nums[i], self.nums[i - 1]
                else:
                    break
            return self.nums[0]




# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
# @lc code=end

