# -- coding: utf-8 --
# author: una
# datetime: 2019-08-04 16:55


# 超时解法，O(K*N*N)
class Solution1:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        当前鸡蛋数为k，层数为n，假设从x层扔鸡蛋：
        1. 如果鸡蛋碎了，则需要在剩下的x-1层中尝试，总次数为：dp(k-1, x-1) + 1
        2. 如果鸡蛋没碎，则需要在剩下的N-x层中尝试，总次数为：dp(k, n-x) + 1
        最坏的情况下的尝试次数应该为：max{dp(k-1, x-1) + 1, dp(k, n-x) + 1}

        上述x的取值范围为1~n，则最坏情况下最少的尝试次数为：min{x=1~n: max{dp(k-1, x-1) + 1, dp(k, n-x) + 1}}
        最终得知确切的F（高于F楼鸡蛋会碎）的值，所需最少尝试次数为：dp(K, N)
        """
        if K == 0 or N == 0:
            return 0
        # 初始化，K+1行，N+1列
        dp = [[0] * (N + 1) for _ in range(K + 1)]
        # 楼层为n，鸡蛋数为1时，解为：n
        for n in range(1, N + 1):
            dp[1][n] = n
        # 鸡蛋数从2开始增加
        for k in range(2, K + 1):
            # 楼层数从1开始增加
            for n in range(1, N + 1):
                dp[k][n] = n
                for x in range(1, n + 1):
                    # 鸡蛋碎了
                    res = dp[k - 1][x - 1] + 1
                    # 鸡蛋没碎
                    res = max(res, dp[k][n - x] + 1)
                    dp[k][n] = min(dp[k][n], res)
        return dp[K][N]


# 降低时间复杂度
class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        """
        设dp[x][k]是移动次数为x，鸡蛋数量为k次时能确定F的最大的楼层数
        假设从n0+1层丢下鸡蛋,
        1. 鸡蛋破了
        剩下x-1次机会和k-1个鸡蛋,可以检测n0层楼
        2. 鸡蛋没破
        剩下x-1次机会和k个鸡蛋,可以检测n1层楼

        那么 临界值层数F在[1,n0+n1+1]中的任何一个值,都都能被检测出来

        归纳的状态转移方程式为:f(x,k) = f(x-1,k-1)+f(x-1,k)+1,即x次移动的函数值可以由x-1的结果推导

        可以简化为dp函数的返回值只跟鸡蛋个数k有关系:
        本次dp(k) = 上次dp(k-1)+上次dp(k)+1
        """
        x = 0
        dp = [0] * (K + 1)  # 1 <= K <= 100
        # dp[k] = n 表示， k个鸡蛋，利用x次移动，最多可以检测n层楼
        while dp[K] < N:
            for k in range(K, 0, -1):
                # 逆序从K---1,dp[i] = dp[i]+dp[i-1] + 1 相当于上次移动后的结果
                # dp[]函数要理解成抽象出来的一个黑箱子函数,跟上一次移动时鸡蛋的结果有关系
                dp[k] += dp[k - 1] + 1
                """
                以上计算式，是从以下转移方程简化而来
                dp[x][k] = 1 + dp[x-1][k-1] + dp[x-1][k]
                假设 dp[x-1][k-1] = n0, dp[x-1][k] = n1
                首先检测，从第 n0+1 楼丢下鸡蛋会不会破。
                如果鸡蛋破了，F 一定是在 [1：n0] 楼中，
                	利用剩下的 x-1 次机会和 k-1 个鸡蛋，可以把 F 找出来。
                如果鸡蛋没破，假如 F 在 [n0+2:n0+n1+1] 楼中
                	利用剩下的 x-1 次机会和 k 个鸡蛋，也可以把 F 找出来。
                所以，当有 x 个放置机会和 k 个鸡蛋的时候
                F 在 [1, n0+n1+1] 中的任何一楼，都能够被检测出来。
                """
            x += 1
        return x
