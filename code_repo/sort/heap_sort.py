# -- coding: utf-8--
# author:Jing
# datetime:2019/6/16 11:02
# software: PyCharm


def heap_sort(nums):
    # 大根堆
    n = len(nums)
    nums = [0] + nums
    # 初始化小根堆：从最后一个非叶结点开始往上调整，自下而上
    for i in range(n // 2, 0, -1):
        heap_adjust(nums, i, n)
    for i in range(n, 1, -1):
        # 将堆顶元素输出（与当前排序数组的最后一个元素nums[i]交换）
        nums[1], nums[i] = nums[i], nums[1]
        # 重新调整最后一个元素之前的数组nums[1:i]
        heap_adjust(nums, 1, i - 1)
    return nums[1:]


def heap_adjust(nums, l, r):
    # 第一个元素有叶子结点时才进行调整，自上而下
    while l <= r // 2:
        t = 2 * l  # l的左子结点
        # 找到两个子结点中较大的那个
        if t < r and nums[t + 1] > nums[t]:
            t += 1
        # 如果父结点大于两个子结点中的较大的那个，则结束调整
        if nums[l] >= nums[t]:
            break
        # 否则：将父结点的值与较大的子结点的值交换，然后调整以t为根结点的子树，使其满足大根堆的条件
        nums[t], nums[l] = nums[l], nums[t]
        l = t


if __name__ == '__main__':
    a = [1, 4, 2, 6, 3, 7, 5, 8]
    print(heap_sort(a))
