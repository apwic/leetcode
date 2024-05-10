class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fraction = []
        n = len(arr)
        
        for i in range(n):
            for j in range(i+1, n):
                fraction.append([arr[i], arr[j]])
                
        fraction = sorted(fraction, key=lambda x: x[0]/x[1])
        return fraction[k-1]