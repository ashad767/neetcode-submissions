class Node:

    def __init__(self, value: int):
        self.children = []
        self.val = value
    

    def search(self, word: str) -> bool:
        if word == "" and len(self.children) == 0:
            return True
        
        if word == "" and len(self.children) > 0:
            return False
        
        is_word_present = False

        for child in self.children:
            if child.val == word[0]:
                is_word_present = is_word_present or child.search(word[1:])
        
        return is_word_present


    def search_prefix(self, word: str) -> bool:
        if word == "":
            return True

        is_word_present = False

        for child in self.children:
            if child.val == word[0]:
                is_word_present = is_word_present or child.search_prefix(word[1:])
        
        return is_word_present


class PrefixTree:

    def __init__(self):
        self.children = {}


    def insert(self, word: str) -> None:
        curr = self.children.get(word[0])

        for i in range(len(word)):
            node = Node(word[i])

            if not curr:
                self.children[word[i]] = node
                curr = node
                continue

            if i == 0:
                continue
            
            curr.children.append(node)
            curr = node
        

    def search(self, word: str) -> bool:
        curr = self.children.get(word[0])

        if not curr:
            return False

        return curr.search(word[1:])


    def startsWith(self, prefix: str) -> bool:
        curr = self.children.get(prefix[0])

        if not curr:
            return False

        return curr.search_prefix(prefix[1:])
