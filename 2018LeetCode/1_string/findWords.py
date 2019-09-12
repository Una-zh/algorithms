# -- coding: utf-8 --
# author: una
# datetime: 2019-08-26 09:46


class Trie_Node:
    def __init__(self, val):
        self.val = val
        self.next = list()
        self.isEnd = False
        self.found = False


class Trie:
    def __init__(self):
        self.root = Trie_Node('')

    def insert(self, word):
        p = self.root
        i = 0
        while i < len(word) and p.next:
            flag = False
            for q in p.next:
                if q.val == word[i]:
                    p = q
                    i += 1
                    flag = True
                    break
            if flag:
                continue
            else:
                break
        while i < len(word):
            tmp = Trie_Node(word[i])
            p.next.append(tmp)
            p = tmp
            i += 1
        p.isEnd = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        width = len(board[0])
        height = len(board)
        trie = Trie()
        for word in words:
            trie.insert(word)
        res = []
        xx = [-1, 1, 0, 0]
        yy = [0, 0, -1, 1]

        def search(x, y, trie_node, vis_str):
            """

            :param x: 当前位置的横坐标
            :param y: 当前位置的纵坐标
            :param trie_node: 上一个已经匹配的结点
            :param vis: 访问矩阵，记录是否访问过（同一个单元格内的字母在一个单词中不允许被重复使用）
            :param vis_str: 已经匹配上的字符串
            :return:
            """
            if not trie_node.next:
                return
            tmp = board[x][y]  # 若board[x][y]匹配，在函数返回之前要还原board[x][y]的值
            for p in trie_node.next:
                if p.val == board[x][y]:
                    board[x][y] = '#'
                    if p.isEnd and not p.found:
                        res.append(vis_str + p.val)
                        p.found = True
                    for i in range(4):
                        tx = x + xx[i]
                        ty = y + yy[i]
                        if tx < 0 or tx >= height or ty < 0 or ty >= width or board[tx][ty] == '#':
                            continue
                        search(tx, ty, p, vis_str + p.val)
                    break
            board[x][y] = tmp

        for i in range(len(board)):
            for j in range(len(board[i])):
                search(i, j, trie.root, '')
        return res


if __name__ == '__main__':

    words = ["oath", "pea", "eat", "rain"]
    board = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]

    # words = ['aa']
    # board = [['a', 'a']]

    # board = [["b", "a", "a", "b", "a", "b"], ["a", "b", "a", "a", "a", "a"], ["a", "b", "a", "a", "a", "b"],
    #          ["a", "b", "a", "b", "b", "a"], ["a", "a", "b", "b", "a", "b"], ["a", "a", "b", "b", "b", "a"],
    #          ["a", "a", "b", "a", "a", "b"]]
    # words = ["bbaabaabaaaaabaababaaaaababb", "aabbaaabaaabaabaaaaaabbaaaba", "babaababbbbbbbaabaababaabaaa",
    #          "bbbaaabaabbaaababababbbbbaaa", "babbabbbbaabbabaaaaaabbbaaab", "bbbababbbbbbbababbabbbbbabaa",
    #          "babababbababaabbbbabbbbabbba", "abbbbbbaabaaabaaababaabbabba", "aabaabababbbbbbababbbababbaa",
    #          "aabbbbabbaababaaaabababbaaba", "ababaababaaabbabbaabbaabbaba", "abaabbbaaaaababbbaaaaabbbaab",
    #          "aabbabaabaabbabababaaabbbaab", "baaabaaaabbabaaabaabababaaaa", "aaabbabaaaababbabbaabbaabbaa",
    #          "aaabaaaaabaabbabaabbbbaabaaa", "abbaabbaaaabbaababababbaabbb", "baabaababbbbaaaabaaabbababbb",
    #          "aabaababbaababbaaabaabababab", "abbaaabbaabaabaabbbbaabbbbbb", "aaababaabbaaabbbaaabbabbabab",
    #          "bbababbbabbbbabbbbabbbbbabaa", "abbbaabbbaaababbbababbababba", "bbbbbbbabbbababbabaabababaab",
    #          "aaaababaabbbbabaaaaabaaaaabb", "bbaaabbbbabbaaabbaabbabbaaba", "aabaabbbbaabaabbabaabababaaa",
    #          "abbababbbaababaabbababababbb", "aabbbabbaaaababbbbabbababbbb", "babbbaabababbbbbbbbbaabbabaa"]
    Solution().findWords(board, words)

# ["aabbbbabbaababaaaabababbaaba","abaabbbaaaaababbbaaaaabbbaab","ababaababaaabbabbaabbaabbaba"]
