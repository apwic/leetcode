class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        for i in range(len(num)):
            max_el = max(num[i:])

            if max_el == num[i]:
                continue

            max_idx = i + "".join(num[i:]).rindex(max_el)
            num[i], num[max_idx] = num[max_idx], num[i]
            break

        return int("".join(num))
        