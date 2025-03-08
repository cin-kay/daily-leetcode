# Link: https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/?envType=daily-question&envId=2025-03-08
# Time: O(n)
# Space: O(1)

def minimum_recolors(blocks: str, k: int) -> int:
  curr_whites = blocks[:k].count("W")
  min_ops = curr_whites

  for i in range(k, len(blocks)):
    if blocks[i - k] == "W":
      curr_whites -= 1
    if blocks[i] == "W":
      curr_whites += 1
    min_ops = min(min_ops, curr_whites)

  return min_ops
  
