class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)
        check = 0

        for ch in target:
            if ch != "_":
                check += 1

        i, j = 0, 0
        count = 0

        while i < n and j < n:
            if start[i] != "_" and target[j] != "_":
                print(i, j)
                print(start[i], target[j])
                if start[i] != target[j]:
                    return False

                # this means "L" can be shifted left
                if start[i] == target[j] == "L":
                    if i - j >= 0:
                        i += 1
                        j += 1
                        count += 1
                        continue
                    else:
                        return False

                # this means "R" can be shifted right
                if start[i] == target[j] == "R":
                    if i - j <= 0:
                        i += 1
                        j += 1
                        count += 1
                        continue
                    else:
                        return False

            if start[i] == "_":
                i += 1

            if target[j] == "_":
                j += 1

        return count == check