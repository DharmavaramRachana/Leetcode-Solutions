class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        changes = defaultdict(int)

        for birth, death in logs:
            changes[birth] += 1
            changes[death] -= 1

        years = sorted(changes.keys())

        curr = 0
        max_pop = 0
        best_year = years[0]

        for y in years:
            curr += changes[y]

            if curr > max_pop:
                max_pop = curr
                best_year = y

        return best_year