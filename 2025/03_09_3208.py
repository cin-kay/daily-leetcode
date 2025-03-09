# Link: https://leetcode.com/problems/alternating-groups-ii/description/?envType=daily-question&envId=2025-03-09
# Time: O(n)
# Space: O(1)

def num_of_alt_groups(colors: list[int], k: int) -> int:
  n = len(colors)
  count = 0
  alt_seq = 1
  last_color = colors[0]

  for i in range(1, n + k - 1):
    idx = i % n
    # check if current color is the same as the last color
    if colors[idx] == last_color:
      alt_seq = 1
      last_color = colors[idx]
      continue

    alt_seq += 1

    if alt_seq >= k:
      count += 1
    
    last_color = colors[idx]

  return count
