# Time: O(n)
# Space: O(1)
# Link: https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/?envType=daily-question&envId=2025-02-22


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recoverFromPreorder(traversal: str) -> TreeNode:
    current_nodes = []

    i = 0
    while i < len(traversal):
        depth = 0
        while i < len(traversal) and traversal[i] == "-":
            depth += 1
            i += 1

        start_value_idx = i
        while i < len(traversal) and traversal[i].isdigit():
            i += 1

        node = TreeNode(val=int(traversal[start_value_idx:i]))

        while len(current_nodes) > depth:
            current_nodes.pop()

        if current_nodes:
            current_nodes: list[TreeNode]
            if not current_nodes[-1].left:
                current_nodes[-1].left = node
            else:
                current_nodes[-1].right = node

        current_nodes.append(node)

    return current_nodes[0]


# Test case
def print_tree(root):
    if not root:
        return None
    return f"[{root.val}, {print_tree(root.left)}, {print_tree(root.right)}]"


test_input = "1-401--349---90--88"
root = recoverFromPreorder(test_input)
print(print_tree(root))
