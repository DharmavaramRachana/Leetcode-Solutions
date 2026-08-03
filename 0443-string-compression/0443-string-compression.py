class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)

        write = 0
        i = 0

        while i < n:
            current_char = chars[i]
            count = 0

            while i < n and chars[i] == current_char:
                count += 1
                i += 1

            chars[write] = current_char
            write += 1

            if count > 1:

                chars_length = str(count)
                for digit in chars_length:
                    chars[write] = digit
                    write += 1

        return write

        