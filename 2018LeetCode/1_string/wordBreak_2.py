# -- coding: utf-8 --
# author: una
# datetime: 2019-08-23 10:13


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 判断是否有解
        if not s:
            return []
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(1, len(s) + 1):
            for word in wordDict:
                if i >= len(word) and s[i - len(word):i] == word and dp[i - len(word)]:
                    dp[i] = True
        res = []
        word_set = set(wordDict)

        # dfs找到所有符合的拆分
        def dfs(pre, start):
            if start == len(s):
                res.append(' '.join(pre))
                return
            for i in range(start + 1, len(s) + 1):
                if s[start:i] in word_set:
                    dfs(pre[:] + [s[start:i]], i)

        # 如果有解，再进行dfs
        if dp[-1]:
            dfs([], 0)

        return res



if __name__ == '__main__':
    # s = 'catsanddog'
    # wordDict = ['cat', 'cats', 'and', 'sand', 'dog']
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s, wordDict))