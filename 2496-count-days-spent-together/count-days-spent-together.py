class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Determine the overlapping date range directly
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        
        if start > end:
            return 0
        
        def to_day(date_str: str) -> int:
            m = int(date_str[:2])
            d = int(date_str[3:])
            return sum(days[:m - 1]) + d
        
        return to_day(end) - to_day(start) + 1