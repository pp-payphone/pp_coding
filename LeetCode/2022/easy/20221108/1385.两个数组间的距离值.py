#
# @lc app=leetcode.cn id=1385 lang=python3
#
# [1385] 两个数组间的距离值
#

# @lc code=start
class Solution:
    # 遍历的时候用二分查找可以更快
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # arr1.sort()
        arr2.sort()
        res = 0
        for n1 in arr1:
            for n2 in arr2:
                if n1 >= n2:
                    if n1 - n2 <= d:
                        # res += 1
                        # print(n1)
                        break
                elif n2 - n1 <= d:
                    # res += 1
                    # print(n1)
                    break
                else:
                    res += 1
                    break
            if n1 >= n2 and n1 - n2 > d:
                res += 1
        return res
# @lc code=end

