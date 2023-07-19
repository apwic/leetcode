class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        merged = [intervals[0]]
        
        for i in range(1, len(intervals)):
            
            if (merged[-1][1] >= intervals[i][0]):
                if (intervals[i][1] >= merged[-1][1]):
                    merged[-1][1] = intervals[i][1]
                continue
                
            if (merged[-1][0] >= intervals[i][0]):
                if (intervals[i][0] <= merged[-1][0]):
                    merged[-1][0] = intervals[i][0]
                continue
                
            merged.append(intervals[i])
                
        return merged