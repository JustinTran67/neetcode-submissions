class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        final = 0
        for i in hash_set:
            if i-1 not in hash_set:
                val = i + 1
                count = 1
                while val in hash_set:
                    count += 1
                    val += 1
                final = max(final, count)
        return final
        