class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        trie = {}
        
        
        best_idx = 0
        for i, w in enumerate(wordsContainer):
            if len(w) < len(wordsContainer[best_idx]):
                best_idx = i
        
        trie["best"] = best_idx

        for i, word in enumerate(wordsContainer):
            node = trie

            
            if self.isBetter(wordsContainer, i, node["best"]):
                node["best"] = i

            for ch in reversed(word):
                if ch not in node:
                    node[ch] = {"best": i}
                node = node[ch]

                if self.isBetter(wordsContainer, i, node["best"]):
                    node["best"] = i

        ans = []

        for query in wordsQuery:
            node = trie
            res = node["best"]

            for ch in reversed(query):
                if ch not in node:
                    break
                node = node[ch]
                res = node["best"]

            ans.append(res)

        return ans

    def isBetter(self, wordsContainer, i, j):
        if len(wordsContainer[i]) != len(wordsContainer[j]):
            return len(wordsContainer[i]) < len(wordsContainer[j])
        return i < j