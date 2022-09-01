#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 我自己搞复杂了呀，第一思路里每个链表到结尾后直接去另一个链表的表头就行，如果相交的话最后一定会同时在相交位置完全相同的！
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        m, n = 1, 1
        p, q = headA, headB
        while p.next:
            m += 1
            p = p.next
        while q.next:
            n += 1
            q = q.next
        if p != q:
            return None
        p, q = headA, headB
        for _ in range(max(m-n, 0)):
            p = p.next
        for _ in range(max(n-m, 0)):
            q = q.next
        while p != q:
            p = p.next
            q = q.next
        return p
# @lc code=end

