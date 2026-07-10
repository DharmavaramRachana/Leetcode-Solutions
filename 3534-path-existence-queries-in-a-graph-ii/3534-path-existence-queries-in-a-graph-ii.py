class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        
        order = sorted(range(n), key=lambda index: nums[index])
        values = [nums[index] for index in order]

        
        position = [0] * n
        for sorted_index, original_index in enumerate(order):
            position[original_index] = sorted_index

        
        next_node = [0] * n
        right = 0

        for left in range(n):
            right = max(right, left)

            while (
                right + 1 < n
                and values[right + 1] - values[left] <= maxDiff
            ):
                right += 1

            next_node[left] = right

        
        component = [0] * n

        for i in range(1, n):
            component[i] = component[i - 1]

            if values[i] - values[i - 1] > maxDiff:
                component[i] += 1

       
        log = max(1, n.bit_length())
        jump = [[0] * n for _ in range(log)]
        jump[0] = next_node

        for level in range(1, log):
            for i in range(n):
                jump[level][i] = jump[level - 1][jump[level - 1][i]]

        answer = []

        for u, v in queries:
            if u == v:
                answer.append(0)
                continue

            left = position[u]
            right = position[v]

            if left > right:
                left, right = right, left

            
            if component[left] != component[right]:
                answer.append(-1)
                continue

            
            if values[left] == values[right]:
                answer.append(1)
                continue

            current = left
            distance = 0

            
            for level in range(log - 1, -1, -1):
                next_position = jump[level][current]

                if next_position < right and next_position > current:
                    current = next_position
                    distance += 1 << level

            
            answer.append(distance + 1)

        return answer