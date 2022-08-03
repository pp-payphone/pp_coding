#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        思路：额外一个m_n的空间后再搬回去
        时间复杂度：O(m+n)
        空间复杂度：O(m+n)
        """
        p = 0
        q = 0
        if n == 0:
            return
        elif m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if n == len(nums2):
            nums2.append(1e12)
        else:
            nums2[n] = 1e12
        if m == len(nums1):
            nums1.append(1e12)
        else:
            nums1[m] = 1e12
        temp = [0 for _ in range(m+n)]
        for i in range(m + n):
            if nums1[p] <= nums2[q]:
                temp[i] = nums1[p]
                p += 1
            else:
                temp[i] = nums2[q]
                q += 1
        for i in range(m + n):
            nums1[i] = temp[i]
        return 
# @lc code=end

s = Solution()
res = s.merge([1,2,3,0,0,0], 3 ,[2,5,6], 3)
res