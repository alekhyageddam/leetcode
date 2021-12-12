class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        if n * k == 0:
            return 0
        
        #sliding window approach with left,right ptrs starting at 0
        left, right = 0,0
        hashmap = {}
        
        max_len = 1
        
        while right < n:
            #add new char and move right ptr until we have at most k distinct characters
            #key is the char, value is the last index at which the char appeared
            hashmap[s[right]] = right
            right += 1
            
            if len(hashmap) == k + 1:
                del_idx = min(hashmap.values())
                del hashmap[s[del_idx]]
                #move left ptr of the slidewindow
                left = del_idx + 1
            
            max_len = max(max_len, right - left)
            
        return max_len
            