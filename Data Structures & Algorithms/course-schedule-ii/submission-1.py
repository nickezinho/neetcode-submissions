class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(list)
        courses = prerequisites
        res = []

        for a, b in courses:
            g[b].append(a)

        states = [0] * numCourses

        def dfs(node):
            state = states[node]
            if state == 2: return True
            elif state == 1: return False

            states[node] = 1

            for n in g[node]:
                if not dfs(n):
                    return False
            
            states[node] = 2

            res.append(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return res[::-1]