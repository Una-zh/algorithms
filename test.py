# -- coding: utf-8--
# author:Jing
# datetime:2019/6/14 11:50
# software: PyCharm

def searchRange(nums, target):
    s = len(nums)
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + ((r - l) >> 1)
        if nums[m] == target:
            s = min(s, m)
        if target <= nums[m]:
            r = m - 1
        else:
            l = m + 1
    e = -1
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + ((r - l) >> 1)
        if nums[m] == target:
            e = max(e, m)
        if target >= nums[m]:
            l = m + 1
        else:
            r = m - 1
    if s == len(nums) or r == -1:
        return [-1, -1]
    else:
        return [s, e]


if __name__ == '__main__':
    # a = [5,7,7,8,8,10]
    # # t = 8
    # # print(searchRange(a, t))
    # for i in a:
    #     print(i, end=' ')
    # import re
    # s = 'abc@124, efg opAs4'
    # res = re.findall(r'[0-9a-zA-Z]', s)
    # print(''.join(res))
    """
    try:
        f = open('myfile.txt')
        s = f.readline()
        i = int(s.strip())
    except IOError:
        print("IO error")
    except ValueError:
        print("ValueError")
    except:
        print("Unexpected error:")
    """
    myList = [2, 3, 4, 1, 7, 6, 8]
    index = 0
    while myList[index] < 7:
        myList[index] += myList[index + 1]
        index += 1
    print(myList)


