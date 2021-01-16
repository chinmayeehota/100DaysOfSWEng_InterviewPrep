"""
Approach:
"""
#Solution using BFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        # map original nodes to their clones
        d = {node : Node(node.val)}
        q = deque([node])

        while q:
         for i in range(len(q)):
             currNode = q.popleft()
             for nei in currNode.neighbors:
                 if nei not in d:
                     # store copy of the neighboring node
                     d[nei] = Node(nei.val)
                     q.append(nei)
                 # connect the node copy at hand to its neighboring nodes (also copies) -------- [1]
                 d[currNode].neighbors.append(d[nei])

        # return copy of the starting node ------- [2]
        return d[node]
        
#Solution using DFS
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return
        d = {node: Node(node.val)}
        stack = [node]
        while stack:
            curNode = stack.pop()
            for nei in curNode.neighbors:
                if nei not in d:
                    d[nei] = Node(nei.val)
                    stack.append(nei)
                d[nei].neighbors.append(d[curNode])
        # return the value of the original node which is a copy of that original node
        return d[node]