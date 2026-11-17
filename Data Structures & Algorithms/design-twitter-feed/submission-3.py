from collections import defaultdict

class Twitter:

    def __init__(self): # O(1)
        self.count = 0 # used to track the age of tweets (greater = more recent)
        self.tweets = defaultdict(list) # userId -> [(count, tweetId)]
        self.following = defaultdict(set) # followerId -> set(followeeId)

    def postTweet(self, userId: int, tweetId: int) -> None: # O(1)
        self.tweets[userId].append((self.count, tweetId))
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]: # O(nlogn)
        # can only see your own tweets and tweets from those you follow
        # appraoch: maintain a minHeap capped at size 10
        res = []
        minHeap = self.tweets[userId].copy() # must create a copy, will edit actual
        for i in self.following[userId]: # go through the set of followees: O(n)
            minHeap.extend(self.tweets[i]) # append the list of tweets to minHeap
        heapq.heapify(minHeap) # O(logn)
        while len(minHeap) > 10:
            heapq.heappop(minHeap) # O(logn)
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return list(reversed(res))

    def follow(self, followerId: int, followeeId: int) -> None: # O(1)
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None: # O(1)
        if followeeId in self.following[followerId]:
            self.following[followerId].discard(followeeId)
