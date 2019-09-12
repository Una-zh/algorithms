# -- coding: utf-8 --
# author: una
# datetime: 2019-09-10 10:38


# 求最长递增子序列的长度
def len_of_LIS(nums):
    if not nums:
        return 0
    res = []
    for x in nums:
        if len(res) == 0:
            res.append([x])
        else:
            if x > res[-1]:
                res.append([x])
            else:
                l, h = 0, len(res)
                while l <= h:
                    m = l + (h - l) // 2
                    # h右侧的都大于等于x，不能判断h位置与x的大小
                    if res[m] >= x:
                        h = m - 1
                    # l左侧的都小于x，不能判断l位置与x的大小
                    else:
                        l = m + 1
                # 查找终止时，l > h，所以第一个比x大的位置是l
                res[l] = x
    return len(res)


# 求最长递增子序列
def LIS(nums):
    if not nums:
        return 0
    res = []
    for x in nums:
        if len(res) == 0:
            res.append([x])
        else:
            if x > res[-1][-1]:
                res.append([x])
            else:
                l, h = 0, len(res)
                while l <= h:
                    m = l + (h - l) // 2
                    # h右侧的都大于等于x，不能判断h位置与x的大小
                    if res[m][-1] >= x:
                        h = m - 1
                    # l左侧的都小于等于x，不能判断l位置与x的大小
                    else:
                        l = m + 1
                # 查找终止时，l > h，所以第一个比x大的位置是l
                res[l].append(x)

    ans = []  # 最终的答案
    for i in res[-1]:
        ans.append([i])
    for i in range(len(res)-2, -1, -1):
        tmp = []
        for d in ans:
            for j in res[i]:
                if j < d[-1]:
                    tmp.append(d[:] + [j])
        ans = tmp

    tmp = []
    for i in ans:
        i.reverse()
        tmp.append(i)

    return tmp


# 求最长非递减子序列的长度
def len_of_LIS_1(nums):
    if not nums:
        return 0
    res = []
    for x in nums:
        if len(res) == 0:
            res.append([x])
        else:
            if x > res[-1]:
                res.append([x])
            else:
                l, h = 0, len(res)
                while l <= h:
                    m = l + (h - l) // 2
                    # h右侧的都大于x，不能判断h位置与x的大小
                    if res[m] > x:
                        h = m - 1
                    # l左侧的都小于等于x，不能判断l位置与x的大小
                    else:
                        l = m + 1
                # 查找终止时，l > h，所以第一个比x大的位置是l
                res[l] = x
    return len(res)


if __name__ == '__main__':
    nums = [1, 2, 6, 7, 9, 3, 13, 4, 6, 10]

    # print(list(reversed(nums)))
    print(LIS(nums))