#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
class Solution:
    # 有没有更高效的算法呢
    # 我也太棒棒了！
    # 还可以用计数排序法！
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # n = len(arr1)
        # p = 0
        # for each in arr2:
        #     for i in range(p, n):
        #         if arr1[i] == each:
        #             arr1[p], arr1[i] = arr1[i], arr1[p]
        #             p += 1
        # tail = arr1[p:]
        # tail.sort()
        # return arr1[:p] + tail

        n = len(arr1)
        m = len(arr2)
        map = {}
        rev_map = {}
        for i, each in enumerate(arr2):
            map[each] = i - m
            rev_map[i - m] = each
        for i, each in enumerate(arr1):
            v = map.get(each)
            if v is not None:
                arr1[i] = v
        arr1.sort()
        for i, each in enumerate(arr1):
            v = rev_map.get(each)
            if v is not None:
                arr1[i] = v
        return arr1
# @lc code=end

