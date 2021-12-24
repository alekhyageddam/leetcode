class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        #sort each interval by start time
        intervals.sort(key = lambda x: x[0])
        
        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                #overlap exists so we merge current and previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged