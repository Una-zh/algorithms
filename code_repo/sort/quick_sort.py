# -- coding: utf-8--
# author:Jing
# datetime:2019/6/15 11:45
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


if __name__ == '__main__':
    a = [4,5,1,6,2,7,3,8]
    quick_sort(a, 0, 7)
    print(a)