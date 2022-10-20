#
# @lc app=leetcode.cn id=744 lang=python3
#
# [744] 寻找比目标字母大的最小字母
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target_ord = ord(target)
        for each in letters:
            if ord(each) > target_ord:
                return each
        return letters[0]
# @lc code=end

