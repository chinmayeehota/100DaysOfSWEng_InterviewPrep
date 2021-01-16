"""
Build the graph as dictionary
- why do we use both res and stack?
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        #build the graph
        graph = collections.defaultdict(list)
        for source, destination in tickets:
            graph[source].append(destination)
            #to add nodes to graph which have no destination
            graph[destination]
        
        for src in graph.keys():
            graph[src].sort(reverse=True)

        stack = []
        res = []
        stack.append("JFK")

        while len(stack) > 0:
            elem = stack[-1]
            if elem in graph and len(graph[elem]) > 0: 
                stack.append(graph[elem].pop())
            else:
                print("res is")
                print(res)
                res.append(stack.pop())
        return res[::-1]