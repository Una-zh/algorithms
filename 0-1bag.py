# -- coding: utf-8 --
# author: una
# datetime: 2019-07-30 11:20

values = [0] + [1, 6, 18, 22, 28]
weights = [0] + [1, 2, 5, 6, 7]
N = len(values) - 1
C = 11
'''
f[i][j]记录当背包承重为j，在面对第i件物品时，背包所装下的最大价值
(N+1) * (C+1) 矩阵初始化
'''
f = [[0] * (C+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, C+1):
        # 要么不装当前物品，要么装当前物品（当前背包重量-当前物品重量）
        if j >= weights[i]:
            f[i][j] = max(f[i-1][j], f[i-1][j-weights[i]] + values[i])
        else:
            f[i][j] = f[i-1][j]

print(f[-1][-1])

for i in range(len(f)):
    for j in range(len(f[0])):
        print(f[i][j], end=' ')
    print('\n')

"""
# 滚动dp
f = [0] * (C+1)
for i in range(1, N+1):
    tmp = [0] * (C+1)
    for j in range(1, C+1):        
        if j >= weights[i]:
            tmp[j] = max(f[j], f[j-weights[i]] + values[i])
        else:
            tmp[j] = f[j]

print(f[-1])
"""