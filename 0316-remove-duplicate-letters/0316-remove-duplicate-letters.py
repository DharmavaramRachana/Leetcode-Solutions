class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_count = {}
        
        # Step 1: count frequency
        for ch in s:
            last_count[ch] = last_count.get(ch, 0) + 1
        
        stack = []
        seen = set()
        
        for ch in s:
            last_count[ch] -= 1
            
            if ch in seen:
                continue
            
            while stack and ch < stack[-1] and last_count[stack[-1]] > 0:
                removed = stack.pop()
                seen.remove(removed)
            
            stack.append(ch)
            seen.add(ch)
        
        return "".join(stack)