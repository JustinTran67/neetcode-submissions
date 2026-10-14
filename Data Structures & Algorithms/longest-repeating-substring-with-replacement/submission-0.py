class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charSet = set(s)
        largest = 0
        for i in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == i:
                    count += 1
                while (r - l + 1) - count > k:
                    if s[l] == i:
                        count -= 1
                    l += 1
                largest = max(largest, r - l + 1)
        return largest