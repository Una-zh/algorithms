# -- coding: utf-8--
# author:Jing
# datetime:2019/6/15 15:51
# software: PyCharm


def shell_sort(nums, dlta):
    for dk in dlta:
        shell_insert(nums, dk)
    return nums


def shell_insert(nums, dk):
    for i in range(dk, len(nums), dk):
        key = nums[i]
        j = i - dk
        while j >= 0 and nums[j] > key:
            nums[j+dk] = nums[j]
            nums[j] = key
            j -= dk


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    dlta = [3,2,1]
    print(shell_sort(a, dlta))