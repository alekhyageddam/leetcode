class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = {}
        for i in range(len(nums)):
            result[nums[i]] = i
        for i in range(len(nums)):
            psbMatch = target - nums[i]
            if psbMatch in result and result[psbMatch] != i:
                return [i, result[psbMatch]]
        return []