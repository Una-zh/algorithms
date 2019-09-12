# -- coding: utf-8--
# author:Jing
# datetime:2019/6/12 10:16
# software: PyCharm
# Definition for singly-linked 2_list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy = ListNode(0)
        t = dummy
        p = l1
        q = l2
        while p and q:
            if p.val <= q.val:
                t.next = p
                p = p.next
            else:
                t.next = q
                q = q.next
            t = t.next
        t.next = p if p is not None else q
        return dummy.next