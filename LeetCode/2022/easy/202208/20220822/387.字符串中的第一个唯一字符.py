#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    # 两次遍历 + hash表可以完成。有没有一次遍历的方法呢？
    def firstUniqChar(self, s: str) -> int:
        m = {}
        for each in s:
            m[each] = m.setdefault(each, 0) + 1
        single = []
        for k, v in m.items():
            if v == 1:
                single.append(k)
        if single:
            for i, each in enumerate(s):
                if each in single:
                    return i
        else:
            return -1
# @lc code=end

