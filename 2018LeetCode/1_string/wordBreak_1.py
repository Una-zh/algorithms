# -- coding: utf-8 --
# author: una
# datetime: 2019-08-19 10:24
from typing import List


# BFS，超时
class Solution_1:
    def __init__(self):
        self.res = False

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words_set = set(wordDict)

        def dfs(remain_s):
            # 剪枝：只需要找到一个拆分方案就可以了
            if self.res:
                return
            # 拆分结束，并且找到了符合条件的拆分
            if not remain_s:
                self.res = True
                return
            for i in range(len(remain_s)-1, -1, -1):
                if remain_s[i:] in words_set:
                    dfs(remain_s[: i])

        dfs(s)
        return self.res


# 动态规划：dp[i]表示s[:i+1]是否可由wordDict中的单词组成，dp[len(s)-1]如果为True，则最终答案为可以
class Solution_2:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s)+1):
            for word in wordDict:
                if i >= len(word) and dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        print(dp)
        return dp[-1]


if __name__ == '__main__':
    # s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    # wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution_2().wordBreak(s, wordDict))