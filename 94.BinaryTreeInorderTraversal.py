from test import test
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        def inorder(node: Optional[TreeNode]) -> None:
            nonlocal result

            if node is None:
                return            
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        
        def preorder(node: Optional[TreeNode]) -> None:
            nonlocal result

            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        def postorder(node: Optional[TreeNode]) -> None:
            nonlocal result

            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        
        inorder(root)
        return result


if __name__ == "__main__":
    test_cases: dict = {
        "Test 1": {
            "args": (),
            "kwargs": {
                "root": TreeNode(val=1, right=TreeNode(val=2, left=TreeNode(val=3)))
            },
            "answer": [1, 3, 2]
        },
        "Test 2": {
            "args": (),
            "kwargs": {
                "root": None
            },
            "answer": []
        },
        "Test 3": {
            "args": (),
            "kwargs": {
                "root": TreeNode(val=1)
            },
            "answer": [1]
        }
    }
    
    test(Solution().inorderTraversal, test_cases)