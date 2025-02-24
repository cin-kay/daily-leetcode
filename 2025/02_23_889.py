# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/?envType=daily-question&envId=2025-02-23
# Time: O(n)
# Space: O(n)


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: "TreeNode | None" = None,
        right: "TreeNode | None" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


def construct_from_pre_post(preorder: list[int], postorder: list[int]) -> TreeNode:
    if not preorder or not postorder:
        return None

    root = TreeNode(preorder[0])
    if len(preorder) == 1:
        return root

    left_size = postorder.index(preorder[1]) + 1  # size in 1-based

    root.left = construct_from_pre_post(
        preorder=preorder[1 : left_size + 1], postorder=postorder[:left_size]
    )
    root.right = construct_from_pre_post(
        preorder=preorder[left_size + 1 :], postorder=postorder[left_size:-1]
    )

    return root


def dump_node(node: TreeNode) -> None:
    if not node:
        return None
    return [node.val, dump_node(node.left), dump_node(node.right)]


preorder = [1, 2, 4, 5, 3, 6, 7]
postorder = [4, 5, 2, 6, 7, 3, 1]

result = construct_from_pre_post(preorder, postorder)
print(dump_node(result))
