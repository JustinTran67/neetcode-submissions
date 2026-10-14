class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        final = []
        for i in nums:
            freq[i] += 1
        for i in range(k):
            max = 0
            maxkey = 0
            for key, value in freq.items():
                if value > max:
                    max = value
                    maxkey = key
            final.append(maxkey)
            del freq[maxkey]
        return final
