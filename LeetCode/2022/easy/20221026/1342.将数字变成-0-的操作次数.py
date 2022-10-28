#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num != 0:
            if num == 1:
                cnt += 1
            elif num % 2 == 1:
                cnt += 2
            else:
                cnt += 1
            num //= 2
        return cnt
# @lc code=end

