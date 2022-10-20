#
# @lc app=leetcode.cn id=953 lang=python3
#
# [953] 验证外星语词典
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        if n == 1:
            return True
        m = {}
        for i, o in enumerate(order):
            m[o] = chr(ord('a') + i)
        m_words = []
        for i, word in enumerate(words):
            m_word = ''
            for each in word:
                m_word += m[each]
            m_words.append(m_word)
        words = [w for w in m_words]
        m_words.sort()
        return words == m_words
# @lc code=end

