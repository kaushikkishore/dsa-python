# https://leetcode.com/problems/design-add-and-search-words-data-structure/

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

        def dfs(idx, root):
            curr = root

            for i in range(idx, len(word)):
                c = word[i]
                if c == ".":
                    # need to search all possibilities here.
                    # options here are backtracking and recursion
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        return dfs(0, self.root)
