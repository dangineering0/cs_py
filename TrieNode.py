class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.val = 0
        self.children = [None] * 26


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    # @void
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        root = self.root

        for c in word:
            indx = ord(c) - ord('a')
            if root.children[indx] is None:
                root.children[indx] = TrieNode()
            root = root.children[indx]
        root.val += 1

    # @returns boolean found
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        found = False
        root = self.root

        for c in word:
            indx = ord(c)-ord('a')
            if root.children[indx] is None:
                return found
            root = root.children[indx]
        return root.val > 0

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        found = False
        root = self.root

        for c in prefix:
            indx = ord(c) - ord('a')
            if root.children[indx] is None:
                return found
            root = root.children[indx]
        return True

t = Trie()

t.insert("abc")

print(t.startsWith("a"))