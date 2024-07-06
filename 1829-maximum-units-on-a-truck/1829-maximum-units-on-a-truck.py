class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key= lambda x: x[1], reverse=True)

        ans = 0
        for i in range(len(boxTypes)):
            if truckSize <= 0:
                break
                
            box, unit = boxTypes[i]
            to_reduce = min(box, truckSize)
            truckSize -= to_reduce
            ans += unit * to_reduce

        return ans
        