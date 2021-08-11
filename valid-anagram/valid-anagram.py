# Two strings are considered anagrams if they are of the same length and contain the same letters.
# from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #solution 1 using Counters collection
            # return Counter(s) == Counter(t)
        
        #hash-table to keep track of counts and catch any edge cases 
        #
        if len(s) != len(t):
            return False
        
        mapping = {}
        
        for char in s:
                mapping[char] = mapping.get(char,0) + 1
        
        for char in t:
            if char in mapping and mapping[char] > 0:
                mapping[char] -= 1
            else:
                return False
        
        return True