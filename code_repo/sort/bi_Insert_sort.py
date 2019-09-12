# -- coding: utf-8--
# author:Jing
# datetime:2019/6/15 15:35
# software: PyCharm
def bi_insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        l, r = 0, i - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if key < nums[m]:
                r = m - 1
            else:
                l = m + 1
        for j in range(i-1, r, -1):
            nums[j+1] = nums[j]
        nums[r+1] = key
    return nums


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    print(bi_insert_sort(a))