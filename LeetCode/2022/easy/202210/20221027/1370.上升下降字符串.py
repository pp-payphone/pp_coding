#
# @lc app=leetcode.cn id=1370 lang=python3
#
# [1370] 上升下降字符串
#

# @lc code=start
class Solution:
    def sortString(self, s: str) -> str:
        cnt_dict = {}
        for each in s:
            cnt_dict[each] = cnt_dict.setdefault(each, 0) + 1
        res = ''
        c = 0
        sort = 1
        ss = 'abcdefghijklmnopqrstuvwxyz'
        while True:
            for each in ss[::sort]:
                cnt = cnt_dict.setdefault(each, 0)
                if cnt > 0:
                    res += each
                    cnt_dict[each] = cnt - 1
                    c += 1
            if c == 0:
                return res
            sort *= -1
            c = 0

# @lc code=end

