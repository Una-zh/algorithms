# -- coding: utf-8 --
# author: una
# datetime: 2019-08-15 17:29
from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        N = len(M)
        father = [i for i in range(N)]

        def find(x):
            if father[x] != x:
                # 压缩路径：把当前查找路径上面的节点直接作为与根节点相连的叶子节点，减少树高而增加树宽
                father[x] = find(father[x])
            return father[x]

        for i in range(N):
            for j in range(i + 1, N):
                if M[i][j] == 1:
                    i_father = find(i)
                    j_father = find(j)
                    if i_father != j_father:
                        father[j_father] = i_father

        for i in range(N):
            father[i] = find(i)

        print(father)
        return len(set(father))


if __name__ == '__main__':
    a = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print(Solution().findCircleNum(a))
