class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        # if no meetings, no rooms needed
        if not intervals:
            return 0
        
        used_rooms = 0
        
        start_times = sorted([interval[0] for interval in intervals])
        end_times = sorted([interval[1] for interval in intervals])
        
        start_ptr = 0
        end_ptr = 0
        
        while start_ptr < len(intervals):
            
            if start_times[start_ptr] >= end_times[end_ptr]:
                used_rooms -= 1
                end_ptr += 1
            
            used_rooms += 1
            start_ptr += 1
        
        return used_rooms