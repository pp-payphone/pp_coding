#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    # 这是一道规则题，考验的是自己的严谨性 O(n) O(1)
    def romanToInt(self, s: str) -> int:
        num_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0
        n = len(s)
        if n == 1:
            return num_dict[s]
        else:
            for i in range(n-1):
                flag = -1 if num_dict[s[i]] < num_dict[s[i+1]] else 1
                res += flag * num_dict[s[i]]
            res += num_dict[s[-1]]
        return res
# @lc code=end

