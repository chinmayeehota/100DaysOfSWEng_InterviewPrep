'''
Approach
Solve using indegree and outdegree concepts
1) Create graph as hashmap mapping source to (time, target)
2) Initialize dictionary with node and "inf" as default distance
3) Start traversing from node k using DFS
'''
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.graph = collections.defaultdict(list)
        for u, v, w in times:
            self.graph[u].append((w, v))
        
        self.dist = {node: float('inf') for node in range(1, n+1)}
        
        self.dfs(k, 0)
        ans = max(self.dist.values())
        return ans if ans < float("inf") else -1
    
    def dfs(self, node, elapsed):
        if elapsed >= self.dist[node]:
            return -1
        self.dist[node] = elapsed
        for time, nei in sorted(self.graph[node]):
            self.dfs(nei, elapsed + time)