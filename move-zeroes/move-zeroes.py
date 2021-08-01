class Solution:
    #O(n) time | O(1) space
    def moveZeroes(self, nums: List[int]) -> None:
        c=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[c],nums[i]=nums[i],nums[c]
                c+=1
        
        