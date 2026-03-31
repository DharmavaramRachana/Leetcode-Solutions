class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        L = n + m - 1
        
        word = ['?'] * L
        fixed = [False] * L   
       
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    p = i + j
                    c = str2[j]
                    if word[p] != '?' and word[p] != c:
                        return ""
                    word[p] = c
                    fixed[p] = True
        
        
        for i in range(L):
            if word[i] == '?':
                word[i] = 'a'
       
        def diff_char(c):
            return 'b' if c == 'a' else 'a'
        
        
        for i in range(n):
            if str1[i] == 'F':
                equal = True
                rightmost_free = -1
                
                for j in range(m):
                    p = i + j
                    if word[p] != str2[j]:
                        equal = False
                        break
                    if not fixed[p]:
                        rightmost_free = p
                
               
                if equal:
                    if rightmost_free == -1:
                        return ""  
                    
                    j = rightmost_free - i
                    word[rightmost_free] = diff_char(str2[j])
        
        return "".join(word)