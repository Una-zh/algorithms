# -- coding: utf-8 --
# author: una
# datetime: 2019-08-24 15:22
import sys


MAX = sys.maxsize


def floyd():
    """

    手动输入：
    n（1~n）：顶点数
    m：边数
    i j d：表示顶点i直达顶点j的距离为d
    :return:
    """
    n, m = map(int, input().strip().split())
    # 邻接表，记录边及距离，{start: {end1: dis1, end2: dis2}}
    adj = [[MAX] * (n+1) for _ in range(n+1)]
    # 记录i到j的路径
    path = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    # 初始化adj和path
    for _ in range(m):
        i, j, k = map(int, input().strip().split())
        adj[i][j] = k
        path[i][j] = [i, j]
    for i in range(1, n+1):
        adj[i][i] = 0

    # 最多只允许经过顶点1 ~ k
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                update = adj[i][k] + adj[k][j]
                if update < adj[i][j]:
                    adj[i][j] = update
                    new_path = path[i][k] + path[k][j]
                    new_path.remove(k)
                    path[i][j] = new_path

    print('----------- shortest distance -----------')
    for i in range(1, len(adj)):
        for j in range(1, len(adj[i])):
            print(adj[i][j], end=' ')
        print('\n')
    print('----------- shortest path -----------')
    for i in range(1, len(path)):
        for j in range(1, len(path[i])):
            print(i, '->', j, ':', path[i][j])


if __name__ == '__main__':
    floyd()


"""
第一行2个数，分别表示顶点数和边数
接下来m条边，每行3个数，分别表示起点、终点、距离
4 8
1 2 2
1 3 6
1 4 4
2 3 3
3 1 7
3 4 1
4 1 5
4 3 12
"""