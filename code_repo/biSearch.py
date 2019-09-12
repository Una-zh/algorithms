# -- coding: utf-8 --
# author: una
# datetime: 2019-09-02 20:00


# 给定一个有序数组（无重复元素或只要找到一个满足的元素），二分查找元素val，找到输出下标，找不到输出-1
def biSearch(nums, val):
    if not nums:
        return -1
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == val:
            return mid
        elif nums[mid] < val:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 给定一个有序数组（可能含有重复的元素），使用二分查找，找出第一个val的下标，找不到则输出-1
def lower_bound(nums, val):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= val:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(nums) and nums[low] == val:
        return low
    else:
        return -1


# 给定一个有序数组（可能含有重复的元素），使用二分查找，找出最后一个val的下标，找不到则输出-1
def upper_bound(nums, val):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= val:
            low = mid + 1
        else:
            high = mid - 1
    if high > -1 and nums[high] == val:
        return high
    else:
        return -1


# lower_bound应用于：求解小于目标元素的最大的元素的位置。
def func1(nums, val):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] >= val:
            high = mid - 1
        else:
            low = mid + 1
    if low < len(nums) and nums[low] == val:
        return low


# upper_bound应用于：求解第一个比目标元素大的元素的位置
def func2(nums, val):
    if not nums:
        return -1
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] <= val:
            low = mid + 1
        else:
            high = mid - 1
    if low > len(nums):
        return -1
    else:
        return low


if __name__ == '__main__':
    a = [1, 2, 2, 2, 3, 4, 5, 6, 7, 8]
    val = 2
    print(upper_bound(a, val))