#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

# @lc code=start
class Solution:
    # 遍历迭代就好
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        a, b = None, None
        res = []
        for i in range(n):
            if i >= 1:
                x = nums[i-1]
            else:
                x = None
            y = nums[i]
            if a is None and b is None:
                a = y
            elif x + 1 != y:
                b = x
                if a == b:
                    res.append("{}".format(a))
                else:
                    res.append('{}->{}'.format(a, b))
                a, b = y, None
            else:
                continue
        if a is not None:
            b = nums[-1]
            if a == b:
                res.append("{}".format(a))
            else:
                res.append('{}->{}'.format(a, b))
        return res

# @lc code=end

