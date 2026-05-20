class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root

        for w in word:
            if curr.children.get(w) is not None:
                curr = curr.children[w]
                continue
        
            node = Node()
            curr.children[w] = node
            curr = node

        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.search_inner(word, self.root)

    def search_inner(self, word: str, curr: Node) -> bool:
        for i in range(len(word)):
            if word[i] != '.' and curr.children.get(word[i]) is None:
                return False
            
            if word[i] != '.':
                curr = curr.children[word[i]]
                continue
            
            isWord = False

            for child in curr.children:
                isWord = isWord or self.search_inner(word[i+1:], curr.children[child])
            
            if not isWord:
                return False

            if isWord:
                return True

        return curr.isEnd
