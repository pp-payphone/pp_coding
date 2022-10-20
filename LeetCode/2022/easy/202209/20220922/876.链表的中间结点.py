#
# @lc app=leetcode.cn id=876 lang=python3
#
# [876] 链表的中间结点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 思路：快慢指针
    def middleNode(self, head: ListNode) -> ListNode:
        p, q = head, head
        c = 0
        while q:
            print(c)
            if c % 2 == 1:
                p = p.next
            q = q.next
            c += 1
        return p
        


# @lc code=end

