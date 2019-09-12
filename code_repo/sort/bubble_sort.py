# -- coding: utf-8--
# author:Jing
# datetime:2019/6/15 18:01
# software: PyCharm


def bubble_sort(nums):
    if len(nums) <= 1:
        return nums
    # 最多进行len(nums)-1趟排序
    for i in range(len(nums)-1):
        # 记录本趟排序是否发生了交换
        cnt = 0
        for j in range(len(nums)-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                cnt += 1
        if cnt == 0:
            break
    return nums


if __name__ == '__main__':
    a = [8,7,6,5,4,3,2,1]
    print(bubble_sort(a))