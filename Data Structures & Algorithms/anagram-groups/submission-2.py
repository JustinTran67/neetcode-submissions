class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j)-ord('a')] += 1
            hashmap[tuple(freq)].append(i)
        return list(hashmap.values())