#
# @lc app=leetcode.cn id=389 lang=python3
#
# [389] 找不同
#

# @lc code=start
class Solution:
    # 两次遍历+额外hash空间肯定是可以的，有没有更优解呢
    # 编码加起来再减再转换
    # 官网思路3：拼接起来的字符串中唯一一个出现奇数次的字符（拼接后做异或运算！）
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for each in t:
            res += ord(each)
        for each in s:
            res -= ord(each)
        return chr(res)
# @lc code=end

