class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i:[] for i in range(numCourses)}
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
        
        cycle = set()

        def dfs(node):
            if node in cycle:
                return False
            if prereq[node] == []:
                return True
            
            cycle.add(node)
            for pre in prereq[node]:
                if dfs(pre) == False:
                    return False
            cycle.remove(node)
            prereq[node] = []
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True