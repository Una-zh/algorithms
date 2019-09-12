# -- coding: utf-8 --
# author: una
# datetime: 2019-09-02 16:09

"""
找第K大的数

"""


# 1. 大根堆
def heap_sort(nums, k):
    """

    :param nums: 无序数组
    :param k: 第k大的数
    :return: 返回第k大的数
    """
    n = len(nums)
    nums = [0] + nums  # 将下标变成从1开始，方便计算
    # 自下而上初始化大根堆
    for i in range(n // 2, 0, -1):
        heap_adjust(nums, i, n)
    print(nums)
    # 输出最大的元素
    nums[1], nums[n] = nums[n], nums[1]
    # 依次输出堆顶元素，然后重新调整（共k-1次），i表示待调整的数组的末尾的下标，n-k取不到
    for i in range(n-1, n-k, -1):
        heap_adjust(nums, 1, i)
        nums[1], nums[i] = nums[i], nums[1]
    return nums[-k]


def heap_adjust(nums, start, end):
    # tmp为需要调整的目标对象，先检查是否需要调整，如果不需要，函数返回
    tmp = start
    # 保证该目标对象有子结点，如果没有子结点了，函数返回
    while tmp <= end // 2:
        t = 2 * tmp  # tmp的左子结点
        if t < end and nums[t+1] > nums[t]:
            t += 1
        if nums[tmp] >= nums[t]:
            break
        else:
            nums[tmp], nums[t] = nums[t], nums[tmp]
            tmp = t


if __name__ == '__main__':
    a = [1, 4, 2, 6, 3, 7, 5, 8]
    k = 3
    print(heap_sort(a, k))
