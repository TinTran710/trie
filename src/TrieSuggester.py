from collections import defaultdict
from src.NameCrawler import NameCrawler

class TrieSuggester:
    def __init__(self):
        self.children = defaultdict(TrieSuggester) # = {'w': TrieSuggester, 'a': TrieSuggester}
        self.isEnd = False

    def insert(self, names):
        for word in names:
            node = self
            for w in word:
                node = node.children[w]
            node.isEnd = True

    def search(self, word):
        node = self
        for w in word:
            if w.lower() in node.children.lower():
                node = node.children[w]
            else:
                return []
        # if prefix match, traverse to all leaf nodes from current node
        result = []
        self.traverse(node, list(word), result) # convert word to a list of characters
        return [''.join(r) for r in result]

    def traverse(self, currentNode, prefix, result):
        if currentNode.isEnd:
            result.append(prefix[:]) # append a copy of prefix (slice of all)
        for character, node in currentNode.children.items(): #  items() returns a list of dict's (key, value) tuple pairs
            prefix.append(character)
            self.traverse(node, prefix, result)
            prefix.pop(-1)