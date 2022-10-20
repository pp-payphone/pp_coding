#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        if n & (n - 1) == 0:
            return 0
        res = 0
        l = 0
        flag = False
        while n != 0:
            if n % 2 == 0:
                n >>= 1
                l += 1
            else:
                if flag:
                    res = max(res, l)
                l = 1
                flag = True
                n >>= 1
        return res
# @lc code=end

