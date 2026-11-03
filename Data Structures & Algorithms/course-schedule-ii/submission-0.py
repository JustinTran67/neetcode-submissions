class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i:[] for i in range(numCourses)}
        for cor, pre in prerequisites:
            prereq[cor].append(pre)
        
        output = []
        visit, cycle = set(), set()

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for pre in prereq[node]:
                if dfs(pre) == False:
                    return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True

        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return output