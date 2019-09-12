# -- coding: utf-8 --
# author: una
# datetime: 2019-08-23 15:47


class Trie_Node:
    def __init__(self, value):
        """

        :param value: 结点的字符值
        :param isEnd: 截止到此处，是否构成关键字
        :param next: 结点的所有子结点（引用）
        """
        self.value = value
        self.isEnd = False
        self.next = list()


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie_Node('')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        pre = self.root
        # 先查找前缀
        i = 0
        while i < len(word):
            flag = False
            for node in pre.next:
                if node.value == word[i]:
                    pre = node
                    flag = True
                    break
            # word[i]匹配到了，继续word中的下一个字符
            if flag:
                i += 1
            # word[i]没匹配到，直接跳出while循环
            else:
                break
        # 插入匹配到的前缀之后的剩余字符
        while i < len(word):
            tmp = Trie_Node(word[i])
            pre.next.append(tmp)
            pre = tmp
            i += 1
        # 将尾字符的isEnd置为True
        pre.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        pre = self.root
        for i in range(len(word)):
            flag = False
            for node in pre.next:
                if node.value == word[i]:
                    pre = node
                    flag = True
                    break
            if not flag:
                return False
        return pre.isEnd  # 最后还要注意下尾字符处是否构成关键词

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        pre = self.root
        for i in range(len(prefix)):
            flag = False
            for node in pre.next:
                if node.value == prefix[i]:
                    pre = node
                    flag = True
                    break
            if not flag:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# ["Trie","insert","search","search","startsWith","insert","search"]
# [[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))

