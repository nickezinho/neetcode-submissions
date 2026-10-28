class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False

        g = defaultdict(list)
        
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()
        def dfs(node, root):
            visited.add(node)

            for n in g[node]:
                if n == root:
                    continue
                if n in visited:
                    return False
                
                if not dfs(n, node):
                    return False
            return True

        if not dfs(0,-1):
            return False
        return len(visited) == n


