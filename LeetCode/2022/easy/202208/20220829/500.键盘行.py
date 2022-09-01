#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
class Solution:
    # 思路上可以用m*n世间复杂度且不用额外的空间的方法，但不想写了
    def findWords(self, words):
        s1 = set(list('qwertyuiop'))
        s2 = set(list('asdfghjkl'))
        s3 = set(list('zxcvbnm'))
        res = []
        for orig_word in words:
            word = list(orig_word.lower())
            a = word[0]
            word = set(word)
            flag = False
            if a in s1 and word.issubset(s1):
                flag = True
            elif a in s2 and word.issubset(s2):
                flag = True
            elif a in s3 and word.issubset(s3):
                flag = True
            if flag:
                res.append(orig_word)
        return res
# @lc code=end

Solution().findWords(["Hello","Alaska","Dad","Peace"])