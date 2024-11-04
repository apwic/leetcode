class Solution:
    def compress(self, chars: List[str]) -> int:
        write, read = 0, 0

        while read < len(chars):
            count = 0
            curr = chars[read]

            while read < len(chars) and curr == chars[read]:
                count += 1
                read += 1

            chars[write] = curr
            write += 1

            if count <= 1:
                continue

            for digit in str(count):
                chars[write] = digit
                write += 1

        return write