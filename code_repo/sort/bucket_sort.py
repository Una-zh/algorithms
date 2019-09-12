# -- coding: utf-8--
# author:Jing
# datetime:2019/6/16 21:51
# software: PyCharm


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def insert(dummy, i):
    p = dummy
    while p.next and p.next.val <= i:
        p = p.next
    q = p.next
    p.next = ListNode(i)
    p.next.next = q


def bucket_sort(nums, m):
    # m是桶的数量
    bucket = [ListNode(0) for _ in range(len(nums))]
    _min = min(nums)
    _max = max(nums)
    interval = (_max - _min) / m
    for i in nums:
        idx = (i - _min) // interval
        insert(bucket[idx], i)
    res = []
    for i in bucket:
        p = i.next
        while p:
            res.append(p.val)
            p = p.next
    return res


if __name__ == '__main__':
    a = [29, 25, 3, 49, 9, 37, 21, 43]
    print(bucket_sort(a, 5))
