class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)
        
        ans = [0] * len(nums)
        for positions in groups.values():
            m = len(positions)
            if m == 1:
                continue
            
            prefix = [0] * (m + 1)
            for i in range(m):
                prefix[i + 1] = prefix[i] + positions[i]
            
            total = prefix[m]
            
            for i, idx in enumerate(positions):
                left = i * idx - prefix[i]
                right = (total - prefix[i + 1]) - (m - i - 1) * idx
                ans[idx] = left + right
        
        return ans