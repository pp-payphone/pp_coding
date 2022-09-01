#
# @lc app=leetcode.cn id=496 lang=python3
#
# [496] 下一个更大元素 I
#

# @lc code=start
class Solution:
    # 官方答案使用了栈的数据结构以计算每个元素后一个更大元素，和我的方法的时间复杂度其实一样一样的
    def nextGreaterElement(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        if m == 0:
            return []
        next_max_dict = {nums2[-1]: -1}
        for i in range(n - 2, -1, -1):
            a, b = nums2[i], nums2[i + 1]
            if a < b:
                next_max_dict[a] = b
            else:
                while a >= b and b != -1:
                    b = next_max_dict[b]
                next_max_dict[a] = b
        res = []
        for each in nums1:
            res.append(next_max_dict[each])
        return res


# @lc code=end

Solution().nextGreaterElement([4,1,2], [1,3,4,2])