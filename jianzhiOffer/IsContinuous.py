# -- coding: utf-8--
# author:Jing
# datetime:2019/6/22 11:03
# software: PyCharm
def quick_sort(arr, low, high):
    if len(arr) <= 1:
        return
    if low < high:
        idx = partition(arr, low, high)
        quick_sort(arr, low, idx - 1)
        quick_sort(arr, idx + 1, high)


def partition(arr, low, high):
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] >= pivot:
            high -= 1
        arr[low] = arr[high]
        while low < high and arr[low] <= pivot:
            low += 1
        arr[high] = arr[low]
    arr[low] = pivot
    return low


class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers) < 2:
            return True
        king = 0
        for i in numbers:
            if i == 0:
                king += 1
        quick_sort(numbers, 0, len(numbers) - 1)
        cnt = 0
        for i in range(king, len(numbers) - 1):
            cnt += numbers[i + 1] - numbers[i] - 1
        return True if cnt <= king else False


if __name__ == '__main__':
    a = [1,3,2,6,4]
    s = Solution()
    print s.IsContinuous(a)