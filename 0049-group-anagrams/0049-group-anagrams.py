class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        group = defaultdict(list)
        sort_strs = []
        
        for word in strs:
            sort_word = ''.join(sorted(list(word)))
            group[sort_word].append(word)
                
        return group.values()
                        
        