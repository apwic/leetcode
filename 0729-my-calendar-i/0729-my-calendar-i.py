import bisect
class MyCalendar:
    def __init__(self):
        self.calendar = []

    def check(self, start, end):
        idx = bisect.bisect_right(self.calendar, (start, end))

        # check next event
        if idx < len(self.calendar) and self.calendar[idx][0] < end:
            return False

        # check previous event
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        return True

    def book(self, start: int, end: int) -> bool:
        if self.check(start, end):
            bisect.insort_right(self.calendar, (start, end))
            return True

        return False
