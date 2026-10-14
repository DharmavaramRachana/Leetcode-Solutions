class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []

        def backtrack(index, path):
            if index == len(s):
                result.append(path)
                return 


            if s[index].isalpha():
                backtrack(index+1, path + s[index].lower())
                backtrack(index+1, path + s[index].upper())

            else:
                backtrack(index+1, path + s[index])

        backtrack(0, "")
        return result

        