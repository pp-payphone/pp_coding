#
# @lc app=leetcode.cn id=1071 lang=python3
#
# [1071] 字符串的最大公因子
#

# @lc code=start
class Solution:
    # 卧槽牛逼；左右拼接和右左拼接如果一样的话就存在子字符串，并且长度正好是最大公约数长度的部分
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        n_min = min(n1, n2)
        n_max = max(n1, n2)
        for length in range(n_min, 0, -1):
            if n_max % length == 0 and n_min % length == 0:
                s = str1[:length]
                flag = True
                for i in range(len(str1) // length):
                    if s != str1[i * length: (i + 1) * length]:
                        flag = False
                        break
                if not flag:
                    break
                for i in range(len(str2) // length):
                    if s != str2[i * length: (i + 1) * length]:
                        flag = False
                        break
                if flag:
                    return s
        return ''
# @lc code=end

Solution().gcdOfStrings("ABABAB", "ABAB")