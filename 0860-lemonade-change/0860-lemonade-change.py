class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        def check(bill):
            if bill == 10:
                if freq[5]:
                    freq[5] -= 1
                    return True
                else:
                    return False
            
            if bill == 20:
                if freq[10] and freq[5]:
                    freq[10] -= 1
                    freq[5] -= 1
                    return True
                elif freq[5]:
                    if freq[5] >= 3:
                        freq[5] -= 3
                        return True
                    else:
                        return False
                else:
                    return False

            return True

        freq = defaultdict(int)

        for bill in bills:
            freq[bill] += 1
            if not check(bill):
                return False

        return True
