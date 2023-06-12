#
# @lc app=leetcode.cn id=1356 lang=python3
#
# [1356] 根据数字二进制下 1 的数目排序
#

# @lc code=start
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        res = []
        d = {}
        s = set()
        for num in arr:
            n = num
            c = 0
            while n != 0:
                c += 1
                n = n & (n - 1)
            s.add(c)
            d[c] = d.setdefault(c, []) + [num]
        l = list(s)
        l.sort()
        for i in l:
            nums = d[i]
            nums.sort()
            res += nums
        return res

# @lc code=end

