from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parents = {i[0] for i in descriptions}
        values: dict = {}

        def create_node(val: int | None) -> TreeNode | None:
            if val is None:
                return None
            children = values.get(val, None)
            if children is None:
                return TreeNode(val=val)
            return TreeNode(val=val, left=create_node(children['left']), right=create_node(children['right']))

        for item in descriptions:
            if item[1] in parents:
                parents.remove(item[1])
            p_children = values.get(item[0], {'left': None, 'right': None})
            if item[-1]:
                p_children['left'] = item[1]
            else:
                p_children['right'] = item[1]
            values[item[0]] = p_children

        head_val = list(parents)[0]

        return create_node(head_val)

