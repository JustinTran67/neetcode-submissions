class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i in range(len(nums)):
            total = 1
            for index, value in enumerate(nums):
                if index == i:
                    continue
                else:
                    total = total * value
            final.append(total)
        return final