# https://leetcode.com/problems/implement-trie-prefix-tree/
from typing import *


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for w in word:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for w in prefix:
            if w not in curr.children:
                return False
            curr = curr.children[w]

        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
param_2 = obj.search("apple")
param_3 = obj.startsWith("app")

print(param_2, param_3)
