class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = {}
        i = 0
        best = 0
        for j, ch in enumerate(s):
            if ch in letters and letters[ch] >= i:
                i = letters[ch] + 1
            letters[ch] = j
            best = max(best, j - i + 1)
        return best