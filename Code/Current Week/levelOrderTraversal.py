'''
Using Queue
- initialize queue to root
- loop while queue is not empty
- pop from que and assign to temp root
- append value of temp root to res array
- add left and right child of temp root in order to queue
- return res after loop exits and that should be the answer
'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        #temp_node = root
        while q:
            temp_node = q.pop(0)
            res.append(temp_node.val)
            if temp_node.left:
                q.append(temp_node.left)
            if temp_node.right:
                q.append(temp_node.right)
        return res