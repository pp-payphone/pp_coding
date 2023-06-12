#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#

# @lc code=start
class Solution:
    def commonChars(self, words):
        n = len(words)
        if n == 1:
            return list(words[0])
        a = list(words[0])
        a.sort()
        for i in range(1, n):
            b = list(words[i])
            b.sort()
            a = self.find_same(a, b)
        return a

    def find_same(self, a, b):
        m, n = len(a), len(b)
        p, q = 0, 0
        res = []
        while p != m and q != n:
            if a[p] == b[q]:
                res.append(a[p])
                p += 1
                q += 1
            elif a[p] < b[q]:
                p += 1
            else:
                q += 1
        return res
# @lc code=end

Solution().commonChars(["bella","label","roller"])