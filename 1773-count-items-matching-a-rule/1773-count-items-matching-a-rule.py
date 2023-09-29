class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:    
        def matchRule(ruleIdx):
            count = 0
            for item in items:
                if ruleValue == item[ruleIdx]:
                     count += 1
                
            return count
            
        if (ruleKey == "type"):
            return matchRule(0)
            
        if (ruleKey == "color"):
            return matchRule(1)
            
        if (ruleKey == "name"):
            return matchRule(2)
            
        