# -- coding: utf-8 --
# author: una
# datetime: 2019-08-24 10:29
from collections import defaultdict
import heapq


MAX = 10**7  # MAX = sys.maxsize


def dijkstra():
    """

    手动输入：
    n（1~n）：顶点数
    m：边数
    s：起点
    i j d：表示顶点i直达顶点j的距离为d
    :return:
    """
    n, m, s = map(int, input().strip().split())
    # 邻接表，记录边及距离，{start: {end1: dis1, end2: dis2}}
    adj = defaultdict(dict)
    # 记录s到其他各个顶点的最短距离
    dis = [MAX] * (n+1)
    # 记录s到其他各个顶点的路径
    path = [[] for i in range(n+1)]
    # 记录已经找到最短路径的顶点
    visited = [False] * (n+1)
    # 输入m条边
    for _ in range(m):
        i, j, d = map(int, input().strip().split())
        adj[i][j] = d

    # 初始化dis和path
    for i in range(1, n+1):
        if i == s:
            dis[i] = 0
            path[i] = [i]
        else:
            if i in adj[s].keys():
                dis[i] = adj[s][i]
                path[i] = [s, i]
    # 记录剩余的(顶点, 距离)元组，方便用堆排序找出当前距离最短的
    heap_dis = set([(v, dis[v]) for v in range(1, n+1)])
    # 开始探索
    visited[s] = True
    # 对其余n-1个顶点，每次求得s到某个顶点v的最短距离，置visited[v]为True
    for _ in range(n-1):
        """
        # 在剩余的顶点中找到当前距离s最近的，O(n)
        min_dis = MAX
        v = None
        for w in range(1, n+1):
            if not visited[w]:
                if dis[w] < min_dis:
                    min_dis = dis[w]
                    v = w
        """
        # 优化：利用小根堆在剩余的顶点中找到当前距离s最近的，O(log n)
        [(v, min_dis)] = heapq.nsmallest(1, heap_dis, key=lambda x: x[1])
        heap_dis.remove((v, min_dis))

        visited[v] = True
        # 更新s到v的所有后继顶点的最短路径if，如果v没有后继顶点，则不更新
        if v in adj.keys():
            for u in adj[v].keys():
                update = dis[v] + adj[v][u]
                if update < dis[u]:
                    dis[u] = update  # 更新最短路径
                    path[u] = path[v] + [u]  # 更新路径
    print('----------- shortest distance -----------')
    print(dis[1:])
    print('----------- shortest path -----------')
    for i in range(1, n+1):
        print(s, '->', i, ':', path[i])


if __name__ == '__main__':
    dijkstra()

"""
第一行3个数，分别表示顶点数、边数、起点
接下来m条边，每行3个数，分别表示起点、终点、距离
4 5 1
1 2 2
1 3 3
2 3 2
3 4 3
2 4 4
"""