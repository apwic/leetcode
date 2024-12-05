class Solution:
    def canChange(self, start: str, target: str) -> bool:
        n = len(start)

        
        start_count, target_count = 0, 0
        for i in range(n):
            if start[i] != "_":
                start_count += 1

            if target[i] != "_":
                target_count += 1

        if start_count != target_count:
            return False
        
        i, j = 0, 0

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
                        continue
                    else:
                        return False

                # this means "R" can be shifted right
                if start[i] == target[j] == "R":
                    if i - j <= 0:
                        i += 1
                        j += 1
                        continue
                    else:
                        return False

            if start[i] == "_":
                i += 1

            if target[j] == "_":
                j += 1

        return True