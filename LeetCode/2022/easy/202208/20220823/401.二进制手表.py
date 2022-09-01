#
# @lc app=leetcode.cn id=401 lang=python3
#
# [401] 二进制手表
#

# @lc code=start
class Solution:
    def readBinaryWatch(self, turnedOn: int):
        up_map = {
            0: ['0'],
            1: ['1', '2', '4', '8'],
            2: ['3', '5', '6', '9', '10'],
            3: ['7', '11']
        }
        down_map = {}
        for num in range(60):
            c = 0
            n = num
            while n != 0:
                c += 1
                n = n & (n - 1)
            down_map[c] = down_map.setdefault(c, []) + ([str(num)] if num > 9 else ['0{}'.format(num)])
        res = []
        for x in range(turnedOn + 1):
            y = turnedOn - x
            for pre in up_map.setdefault(x, []):
                for tail in down_map.setdefault(y, []):
                    res.append('{}:{}'.format(pre, tail))
        return res
# @lc code=end

Solution().readBinaryWatch(1)