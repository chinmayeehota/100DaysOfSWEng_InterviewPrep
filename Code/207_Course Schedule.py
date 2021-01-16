class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.visited = [0] * numCourses
        
        # Build the graph.
        self.graph = collections.defaultdict(list)
        for postreq, course in prerequisites:
            self.graph[course].append(postreq)
            self.graph[postreq]  # Make sure nodes are made for courses with no postreqs.
        
        if not prerequisites:
            return True
        #Traverse the graph calling DFS from each node
        for node in self.graph:
            if not self.visited[node]:
                if not self.depthFirstSearch(node):
                    return False
        return True
        
     
    def depthFirstSearch(self, node):
        if self.visited[node] == 1:
            return False
        
        self.visited[node] = 1
        
        for neighbour in self.graph[node]:
            print(self.graph)
            print(self.visited)
            if self.visited[neighbour] != 2 and not self.depthFirstSearch(neighbour):
                return False
        self.visited[node] = 2
        return True