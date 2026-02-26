class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        level = 0
        gene_chars = ['A','G','T','C']

        q = deque()
        q.append(startGene)
        bank_set = set(bank)

        while q:
            size = len(q)
            level += 1

            for _ in range(size):
                current = list(q.popleft())

                for pos in range(8):
                    original = current[pos]

                    for c in gene_chars:
                        current[pos] = c
                        mutated = "".join(current)

                        if mutated == endGene and mutated in bank:
                            return level

                        if mutated in bank_set:
                            bank_set.remove(mutated)
                            q.append(mutated)

                    current[pos] = original


        return -1