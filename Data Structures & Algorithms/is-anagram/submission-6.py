from collections import Counter

# {r:1 a:2 t: 1} -> -1 for every found in other str
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = Counter(s)
        for i in t:
            if i in freq1:
                freq1[i] -= 1
                if freq1[i] < 0:
                    return False
            else:
                return False
        for val in freq1.values():
            if val != 0:
                return False
        return True
