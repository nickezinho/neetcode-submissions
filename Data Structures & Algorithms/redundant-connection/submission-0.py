class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        g = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True

            visited.add(node)
            for n in g[node]:
                if n not in visited:
                    if dfs(n, target, visited):
                        return True
            return False
        
        for a, b in edges:

            if dfs(a, b, set()):
                return [a,b]
            g[a].append(b)
            g[b].append(a)




        
            