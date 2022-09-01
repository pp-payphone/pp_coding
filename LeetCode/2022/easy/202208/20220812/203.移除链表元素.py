#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 隐藏头
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        pre = ListNode(0,next=head)
        if head is None:
            return head
        p = pre
        while p.next is not None:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return pre.next
        
# @lc code=end

