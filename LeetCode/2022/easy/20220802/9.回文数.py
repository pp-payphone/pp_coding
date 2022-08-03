#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    # 变为字符串，从左从右分别匹配判断 O(n) O(n)
    # 不变为字符串的思路：尾部取余，头部取模
    # 官方思路是有意思的，值得借鉴的，从尾部开始翻转整个数字，理论上翻转一半后如果和剩下的一样那就是回文的。而通过翻转后和剩下的大小比较可以知道是否翻转到了一半。这里主要是为了防止翻转后溢出内存，但python其实没有这个问题，同时溢出后就说明一定不是回文。(但这种写法下容易有小bug，需要好好检查)
    # 个人认为官方写法的复杂度是O(n) O(1)
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        b = 0
        a = x
        while b < a:
            b = b * 10 + a % 10
            aa = a
            a = a // 10
        if b == a or b == aa:
            return True
        else:
            return False
# @lc code=end

Solution().isPalindrome(10)