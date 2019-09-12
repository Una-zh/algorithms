# -- coding: utf-8 --
# author: una
# datetime: 2019-09-02 10:55


MOD = 1e9 + 7


def qpow(base, n):
    # 求：base ** n
    ans = 1
    while n:
        # 取n的二进制的最低位，为1时将ans乘以base
        if n & 1:
            ans = ans * base % MOD
        # base每平方一次，n要右移一位
        base = base * base % MOD
        n = n >> 1
    return ans


"""
example
3 ** 11
11 = (1011)_2 = 2 ** 0 + 2 ** 1 + 2 ** 3
3 ** 11 = [3 ** (2 ** 0)] * [3 ** (2 ** 1)] * [3 ** (2 ** 3)]
"""


def divide_mod(a, b):
    # 求：(b / a) % MOD
    return ((b + MOD) % MOD) * qpow((a + MOD) % MOD, MOD - 2) % MOD