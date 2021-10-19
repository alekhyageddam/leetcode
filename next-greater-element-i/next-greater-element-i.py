class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        elements = {}
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                elements[stack.pop()] = nums2[i]
            #if element is smaller than the previous element, add it to the stack
            stack.append(nums2[i])
        #after we loop through nums2 arr, the element in stack is the greatest elem so we assign -1
        for key in stack:
            elements[key] = -1
        return [elements[key] for key in nums1]