# Link: https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
# Time: O(n)
# Space: O(n)

# I made this but thanks to ChatGPT :)

import math
from collections import defaultdict


class Solution:
    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        n = len(amount)
        tree = defaultdict(list)
        parent = [0] * n
        aliceDist = [-1] * n

        # Build the tree as an adjacency list
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # DFS to calculate Alice's distance from the root and record parents
        def dfs_alice(node, prev, depth):
            parent[node] = prev
            aliceDist[node] = depth
            for neighbor in tree[node]:
                if neighbor != prev:
                    dfs_alice(neighbor, node, depth + 1)

        dfs_alice(0, -1, 0)

        # Adjust amounts based on Bob's path to the root
        current = bob
        bobDist = 0
        while current != 0:
            if bobDist < aliceDist[current]:
                amount[current] = 0  # Bob opens the gate before Alice arrives
            elif bobDist == aliceDist[current]:
                amount[current] //= 2  # Alice and Bob arrive simultaneously
            current = parent[current]
            bobDist += 1

        # DFS to find the maximum profit path for Alice
        def dfs_max_profit(node, prev):
            max_child_profit = -math.inf
            is_leaf = True
            for neighbor in tree[node]:
                if neighbor != prev:
                    is_leaf = False
                    max_child_profit = max(
                        max_child_profit, dfs_max_profit(neighbor, node)
                    )
            if is_leaf:
                return amount[node]
            return amount[node] + max_child_profit

        return dfs_max_profit(0, -1)


# Example usage:
edges = [[0, 1], [1, 2], [1, 3], [3, 4]]
bob = 3
amount = [-2, 4, 2, -4, 6]

print(Solution().mostProfitablePath(edges, bob, amount))  # 6
