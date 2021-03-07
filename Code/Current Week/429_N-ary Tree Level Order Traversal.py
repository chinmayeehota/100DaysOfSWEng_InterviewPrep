class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        q = [root]
        res = []
        
        #temp_node = root
        while q:
            res_temp = []
            for _ in range(len(q)):
                temp_node = q.pop(0)
                res_temp.append(temp_node.val)
                if temp_node.children:
                    for child in temp_node.children:
                        q.append(child)
            res.append(res_temp)
        return res