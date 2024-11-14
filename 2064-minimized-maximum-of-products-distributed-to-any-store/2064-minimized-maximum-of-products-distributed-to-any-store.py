class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def distribute(k, store=n):
            for quantity in quantities:
                div, rem = quantity // k, quantity % k
                store -= div

                if rem:
                    store -= 1

            return store >= 0

        l, r = 1, max(quantities)
        while l <= r:
            mid = l + (r-l) // 2
            check = distribute(mid)
            if check:
                r = mid - 1
            else:
                l = mid + 1

        return l