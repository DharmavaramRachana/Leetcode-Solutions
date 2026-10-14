class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = [""]

        for ch in s:
            temp = []

            if ch.isalpha():
                for word in result:
                    temp.append(word + ch.lower())
                    temp.append(word + ch.upper())

            else:
                for word in result:
                    temp.append(word + ch)

            result = temp

        return result

        