#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
class Solution:
    # 是2的幂且末尾为4,6
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        if (2 ** 32) % n == 0 and n % 10 in [4, 6]:
            return True
        return False
# @lc code=end

