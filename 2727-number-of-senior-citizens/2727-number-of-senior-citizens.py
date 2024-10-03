class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return len([detail for detail in details if int(detail[11:13]) > 60])