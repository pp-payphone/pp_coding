#
# @lc app=leetcode.cn id=1455 lang=python3
#
# [1455] 检查单词是否为句中其他单词的前缀
#

# @lc code=start
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        m = len(searchWord)
        for i, each in enumerate(sentence.split(' ')):
            if len(each) >= m and each[:m] == searchWord:
                return i + 1
        return -1
# @lc code=end

