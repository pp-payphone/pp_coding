#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    # 这不就是倒着遍历一下么。。。 O(n) O(1)
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n-1, -1, -1):
            if res != 0 and s[i] == ' ':
                return res
            elif s[i] != ' ':
                res += 1
        return res
# @lc code=end

Solution().lengthOfLastWord("   fly me   to   the moon  ")