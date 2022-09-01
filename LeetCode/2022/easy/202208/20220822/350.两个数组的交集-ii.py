#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_m = {}
        for each in nums1:
            nums1_m[each] = nums1_m.setdefault(each, 0) + 1
        res = []
        for each in nums2:
            cnts = nums1_m.get(each)
            if cnts:
                res.append(each)
                nums1_m[each] = cnts - 1
        return res
        # 进阶
        # 排好序如何优化：两个指针直接遍历就可以
        # nums1更小如何优化：直接遍历比较好
        # 更是我这种方法了
# @lc code=end

