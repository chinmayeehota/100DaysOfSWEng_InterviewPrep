'''
'''
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        self.res = []
        self.postorderHelper(root, self.res)
        return self.res
    
    def postorderHelper(self, node, res):
        if node is not None:
            if node.children:
                for child in node.children:
                    self.postorderHelper(child, res)
            res.append(node.val)
        return