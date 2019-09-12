# -- coding: utf-8 --
# author: una
# datetime: 2019-08-18 12:59

res = list()
N = int(input().strip())


def generate(left, right, s):
    if N == 0:
        return
    if len(s) == 2 * N:
        res.append(s)
        return
    elif left == 0:
        generate(left, right-1, s+')')
    else:
        if right == left:
            generate(left-1, right, s+'(')
        else:
            generate(left-1, right, s+'(')
            generate(left, right-1, s+')')


generate(N, N, '')
print(res)


