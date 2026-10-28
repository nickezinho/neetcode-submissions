class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)

        for a, b in edges:
            g[a].append(b)
            g[b].append(a)

        visited = set()
        count = 0

        def dfs(node):
            visited.add(node)

            for n in g[node]:
                if n not in visited:
                    dfs(n)

        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)
            
            
        return count


        
            

                

        