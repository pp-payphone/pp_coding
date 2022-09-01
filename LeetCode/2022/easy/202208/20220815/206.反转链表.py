#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # 我去啊，居然想不出来这玩意儿要怎么递归
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代思路 O(n) O(1)
        # 先4-5再3-4
        # if head is None:
        #     return None
        # if head.next is None:
        #     return head
        # p, q, w = head, head.next, head.next.next
        # p.next = None
        # while w is not None:
        #     q.next = p
        #     p, q = q, w
        #     w = q.next
        # q.next = p
        # return q

        # 递归思路
        # 递归思路虽然效率低，但是和有意思，我还真没想到这么去做递归 O(n) O(n)
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head

        
# @lc code=end

