#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s = 0
        d = {}
        res = []
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if d.get(num) is None:
                d[num] = 1
                s += num
            else:
                res.append(num)
                s += sum(nums[i:])
                break
        res.append(int(n * (n + 1) / 2 - s + num))
        return res

# @lc code=end

