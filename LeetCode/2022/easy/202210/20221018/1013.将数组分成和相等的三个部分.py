#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#

# @lc code=start
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        s = sum(arr)
        if s % 3 != 0:
            return False
        ss = s // 3
        r = 0
        c = 0
        for i, a in enumerate(arr):
            r += a
            if r == ss:
                c += 1
                r = 0
            if c == 2 and i != n - 1:
                return True
        return False

# @lc code=end

