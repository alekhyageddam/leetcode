class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # uniqueNumbers = set(nums)
        # sorted(uniqueNumbers, reverse=True)
        # for i in range(len(nums)):
        #     foundidx = k + 1
        #     if i == foundidx:
        #         return nums[i]
        nums.sort(reverse=True)
        return nums[k-1]

        