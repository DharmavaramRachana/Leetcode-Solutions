class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: x[1] - x[0], reverse=True)

        energy = 0
        initial = 0

        for actual, minimum in tasks:
            if energy < minimum:
                need = minimum - energy
                initial += need
                energy += need

            energy -= actual

        return initial