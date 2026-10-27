class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        courses = prerequisites

        for a, b in courses:
            g[a].append(b)

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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
        