#Iterative
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue, q_temp, res,res_temp = [], [], [], []
        if root:
            queue.append([root])
        else:
            return []
        while len(queue[0]) != 0:
            nodes = queue.pop(0)
            for node in nodes:
                res_temp.append(node.val)
                
                if node.left:
                    q_temp.append(node.left)
                    
                if node.right:
                    q_temp.append(node.right)
                
            queue.append(q_temp)
            q_temp = []
            res.append(res_temp)
            res_temp = []
            
        return res