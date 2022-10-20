#
# @lc app=leetcode.cn id=929 lang=python3
#
# [929] 独特的电子邮件地址
#

# @lc code=start
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        diff_set = set()
        for email in emails:
            a_, b_ = email.split('@')
            a = ''
            for each in a_:
                if each == '+':
                    break
                elif each == '.':
                    continue
                else:
                    a += each
            diff_set.add(a + '@' + b_)
        return len(diff_set)
# @lc code=end

