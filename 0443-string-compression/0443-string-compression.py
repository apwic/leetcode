class Solution:
    def compress(self, chars: List[str]) -> int:
        before = chars[0]
        count = 1
        start_idx = 1
        curr_idx = 1

        while curr_idx < len(chars):
            if before == chars[curr_idx]:
                count += 1
                curr_idx += 1
                continue

            digits = []
            if count > 1:
                del chars[start_idx:curr_idx]
                digits = list(str(count))
                chars[start_idx:start_idx] = digits
                curr_idx = start_idx + len(digits) 

            count = 1    
            before = chars[curr_idx]
            curr_idx += 1
            start_idx = curr_idx

        if count > 1:
            chars[start_idx:] = list(str(count))

        return len(chars)