#
# @lc app=leetcode.cn id=728 lang=python3
#
# [728] 自除数
#

# @lc code=start
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []

        def f(num):
            orig_n = num
            while num != 0:
                t = num % 10
                if t == 0:
                    return False
                if orig_n % t != 0:
                    return False
                num //= 10
            return True

        for num in range(left, right + 1):
            if f(num):
                res.append(num)
        return res
# @lc code=end

