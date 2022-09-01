#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#

# @lc code=start
class Solution:
    # O(1) ?
    # 数根与数模9同余
    def addDigits(self, num: int) -> int:
        # while num >= 10:
        #     res = 0
        #     for n in str(num):
        #         res += int(n)
        #     num = res
        # return num
        return (num - 1) % 9 + 1 if num else 0
# @lc code=end

