#
# @lc app=leetcode.cn id=1089 lang=python3
#
# [1089] 复写零
#

# @lc code=start
class Solution:
    def duplicateZeros(self, arr) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        cp = [_ for _ in arr]
        p = 0
        q = 0
        f = False
        while p < n:
            if f:
                arr[p] = 0
                p += 1
                f = False
            elif cp[q] != 0:
                arr[p] = cp[q]
                p += 1
                q += 1
            else:
                arr[p] = 0
                p += 1
                q += 1
                f = True
        return
# @lc code=end

Solution().duplicateZeros([1,0,2,3,0,4,5,0])