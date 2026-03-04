class TrieNode:
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        root = TrieNode()

        for product in products:
            node = root
            for c in product:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

                if len(node.suggestions) < 3:
                    node.suggestions.append(product)

        
        res = []
        node = root
        for c in searchWord:
            if node and c in node.children:
                node = node.children[c]
                res.append(node.suggestions)
            else:
                node = None
                res.append([])

        return res


        