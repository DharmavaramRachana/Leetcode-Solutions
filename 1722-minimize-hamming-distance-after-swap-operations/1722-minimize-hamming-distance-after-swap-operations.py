class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return
            
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

       
        for a, b in allowedSwaps:
            union(a, b)

        
        groups = defaultdict(list)
        for i in range(n):
            groups[find(i)].append(i)

        hamming = 0

       
        for indices in groups.values():
            freq = Counter(source[i] for i in indices)

            for i in indices:
                if freq[target[i]] > 0:
                    freq[target[i]] -= 1
                else:
                    hamming += 1

        return hamming