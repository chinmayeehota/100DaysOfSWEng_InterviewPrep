'''
Idea is to traverse level order and reverse alternate lists
''' 
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
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
            if len(res) % 2 == 0:
                res.append(res_temp)
            else:
                res.append(reversed(res_temp))
            res_temp = []
        return res