# -- coding: utf-8--
# author:Jing
# datetime:2019/6/15 15:04
# software: PyCharm


def insert_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            nums[j] = key
            j -= 1
    return nums


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    print(insert_sort(a))