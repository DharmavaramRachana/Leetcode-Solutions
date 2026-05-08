class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        mx = max(nums)

        # Smallest Prime Factor sieve
        spf = list(range(mx + 1))

        for i in range(2, int(mx ** 0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, mx + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            factors = set()

            while x > 1:
                p = spf[x]
                factors.add(p)

                while x % p == 0:
                    x //= p

            return factors

        # prime factor -> indices
        factor_map = defaultdict(list)

        for i, val in enumerate(nums):
            for p in get_factors(val):
                factor_map[p].append(i)

        q = deque([0])
        visited = {0}
        used_prime = set()

        steps = 0

        while q:

            for _ in range(len(q)):
                i = q.popleft()

                if i == n - 1:
                    return steps

                # adjacent jumps
                for nei in [i - 1, i + 1]:
                    if 0 <= nei < n and nei not in visited:
                        visited.add(nei)
                        q.append(nei)

                # prime teleport
                val = nums[i]

                # teleport only if nums[i] itself is prime
                if val > 1 and spf[val] == val and val not in used_prime:

                    for nei in factor_map[val]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)

                    used_prime.add(val)

            steps += 1

        return -1