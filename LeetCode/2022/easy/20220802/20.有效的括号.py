#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    # 栈，先进后出 O(n) O(n)
    def isValid(self, s: str) -> bool:
        d = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        l = []
        for each in s:
            if each in ['[', '{', '(']:
                l.append(each)
            else:
                if l == []:
                    return False
                left = l.pop()
                if d[left] != each:
                    return False
        if l == []:
            return True
        else:
            return False
# @lc code=end

Solution().isValid("()")