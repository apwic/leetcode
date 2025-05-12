class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = Counter(list(map(str,digits)))
        def check(num):
            num = Counter(str(num))

            for key, val in num.items():
                if val > freq[key]:
                    return False

            return True

        ans = []
        numbers = [num for num in range(100, 1000) if num % 2 == 0]
        for num in numbers:
            if check(num):
                ans.append(num)

        return ans