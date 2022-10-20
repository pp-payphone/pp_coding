#
# @lc app=leetcode.cn id=821 lang=python3
#
# [821] 字符的最短距离
#

# @lc code=start
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        target_index = []
        for idx, each in enumerate(s):
            if each == c:
                target_index.append(idx)
        m = len(target_index)
        p = 0
        low_index = None
        up_index = target_index[p]
        res = []
        for i in range(n):
            if up_index is None:
                res.append(i - low_index)
            elif i < up_index:
                if low_index is None:
                    res.append(up_index - i)
                else:
                    res.append(min(up_index - i, i - low_index))
            else:
                res.append(0)
                low_index = up_index
                p += 1
                if p < m:
                    up_index = target_index[p]
                else:
                    up_index = None
        return res


# @lc code=end

