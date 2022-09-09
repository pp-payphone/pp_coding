#
# @lc app=leetcode.cn id=717 lang=python3
#
# [717] 1 比特与 2 比特字符
#

# @lc code=start
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if bits[-1] == 1:
            return False
        n = len(bits)
        if n == 1:
            return True
        p = 0
        while p < n - 1:
            if bits[p] == 0:
                p += 1
            else:
                p += 2
        return p == n - 1
# @lc code=end

