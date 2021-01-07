'''
Traversing the tree using level order traversal
For each level the last node of that level is visible in right-side view
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        queue = []
        queue_temp = []
        res = []
        res_temp = []
        if root:
            queue.append([root])
        else:
            return []
        while queue[0]:
            nodes = queue.pop(0)
            for node in nodes:
                res_temp.append(node.val)
                if node.left:
                    queue_temp.append(node.left)
                if node.right:
                    queue_temp.append(node.right)
            queue.append(queue_temp)
            queue_temp = []
            res.append(res_temp[-1])
            res_temp = []
        return res