#
# @lc app=leetcode.cn id=459 lang=python3
#
# [459] 重复的子字符串
#

# @lc code=start
class Solution:
    # 思路：第一思路都是O(n*n)时间复杂度的遍历解法，有没有更快的？
    # 第二层遍历可以只对因子项去做判断
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n == 1:
            return False
        for repeat_len in range(1, n // 2 + 1):
            if n % repeat_len != 0:
                continue
            flag = True
            for blocks in range(n // repeat_len):
                if s[blocks * repeat_len: (blocks + 1) * repeat_len] != s[0: repeat_len]:
                    flag = False
                    break
            if flag:
                return True
        return False


# @lc code=end

