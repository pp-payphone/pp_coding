#
# @lc app=leetcode.cn id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1, n + 1):
            f1 = (i % 3 == 0)
            f2 = (i % 5 == 0)
            if f1 and f2:
                res.append('FizzBuzz')
            elif f1:
                res.append('Fizz')
            elif f2:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res
            
# @lc code=end

