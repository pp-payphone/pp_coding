#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] 赎金信
#

# @lc code=start
class Solution:
    # 我太强了，我就是标答
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = len(ransomNote)
        n = len(magazine)
        if m > n:
            return False
        d = {}
        for word in ransomNote:
            d[word] = d.setdefault(word, 0) - 1
        for word in magazine:
            d[word] = d.setdefault(word, 0) + 1
        for value in d.values():
            if value < 0:
                return False
        return True
# @lc code=end

