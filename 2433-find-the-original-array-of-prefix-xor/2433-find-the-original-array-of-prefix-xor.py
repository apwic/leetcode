class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prefsum = [pref[0]]
        res = [pref[0]]
        
        for i in range(1, len(pref)):
            res.append(prefsum[i-1] ^ pref[i])
            prefsum.append(prefsum[i-1] ^ res[-1])
        
        return res