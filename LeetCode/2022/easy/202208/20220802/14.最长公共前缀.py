#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    # 第一直觉是遍历 O(nm) O(1)
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            idx = 0
            flag = True
            while flag:
                s = ''
                for each in strs:
                    if len(each) <= idx:
                        flag = False
                        break
                    if s == '':
                        s = each[idx]
                    else:
                        if each[idx] != s:
                            flag = False
                            break
                if flag:
                    
                    idx += 1
        return strs[0][:idx]
# @lc code=end

Solution().longestCommonPrefix(["flower","flow","flight"])