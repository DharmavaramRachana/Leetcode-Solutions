class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        pref = [0]
        s = 0
        for x in nums:
            s += 1 if x == target else -1
            pref.append(s)

        vals = sorted(set(pref))
        rank = {v: i + 1 for i, v in enumerate(vals)}

        m = len(vals)
        bit = [0] * (m + 1)

        def update(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for x in pref:
            r = rank[x]
            ans += query(r - 1)  # previous prefix sums < x
            update(r)

        return ans