class Solution:
    def splitStr(self, time: str) -> int:
        time = time.split(":")
        hour = int(time[0])
        minute = int(time[1])
        
        return hour*60 + minute
        
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        event1[0], event1[1] = self.splitStr(event1[0]), self.splitStr(event1[1])
        event2[0], event2[1] = self.splitStr(event2[0]), self.splitStr(event2[1])
        events = [event1, event2]
        
        if (event1[1] > event2[1]):
            events[0], events[1] = events[1], events[0]
            
        if (events[0][1] >= events[1][0]):
            return True
        
        return False