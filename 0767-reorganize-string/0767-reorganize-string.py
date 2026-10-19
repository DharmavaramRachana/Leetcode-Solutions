class Solution:
    def reorganizeString(self, s: str) -> str:
        if not s:
            return ""

        count = {}

        for char in s:
            count[char] = 1 + count.get(char, 0)

        most_frequent = max(count, key = count.get)
        n = len(s)

        if count[most_frequent] > (n + 1) //2:
            return ""

        result = [0] * n
        index = 0


        for _ in range(count[most_frequent]):
            result[index] = most_frequent
            index += 2

        count[most_frequent] = 0

        for char in count:
            for _ in range(count[char]):
                if index >= n:
                    index = 1

                result[index] = char
                index += 2

        return "".join(result)
