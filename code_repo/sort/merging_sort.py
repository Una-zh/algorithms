# -- coding: utf-8--
# author:Jing
# datetime:2019/6/16 15:39
# software: PyCharm


def merge(l, r):
    # 将l和r归并，并返回
    res = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    res += l[i:]
    res += r[j:]
    return res


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    m = len(nums) // 2
    l = merge_sort(nums[:m])
    r = merge_sort(nums[m:])
    return merge(l, r)


if __name__ == '__main__':
    a = [1, 4, 2, 6, 3, 7, 5, 8]
    print(merge_sort(a))