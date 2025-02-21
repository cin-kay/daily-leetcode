# Time: __init__: O(n), find: O(1)


# Solution: 2025/02_21_1261.py
# Link: https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/?envType=daily-question&envId=2025-02-21
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: TreeNode | None):
        self.values = set()

        def recover(node: TreeNode | None, val: int):
            if not node:
                return
            node.val = val
            self.values.add(val)
            recover(node.left, 2 * val + 1)
            recover(node.right, 2 * val + 2)

        recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.values


root = TreeNode(-1, right=TreeNode(-1))
find_elements = FindElements(root)
print(find_elements.find(1))
print(find_elements.find(2))
