'''
when to graph coloring technique

Reference
https://leetcode.com/problems/is-graph-bipartite/discuss/115543/Easy-Python-Solution

https://leetcode.com/problems/is-graph-bipartite/discuss/115493/Python-7-lines-DFS-graph-coloring-w-graph-and-Explanation

'''

#solution using dfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def dfs(x, c):
            if x in color: return color[x] == c
            color[x] = c
            return all(dfs(y, -c) for y in graph[x])
        
        return all(i in color or dfs(i, 1) for i in range(len(graph)))

#solution using bfs
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = {}
        def bfs(x):
            q = deque([x])
            color[x] = 1
            while q:
                cur = q.popleft()
                for n in graph[cur]:
                    if n not in color:
                        color[n] = -color[cur]
                        q += n,
                    elif color[n] == color[cur]:
                        return False
            return True
        
        return all(i in color or bfs(i) for i in range(len(graph)))