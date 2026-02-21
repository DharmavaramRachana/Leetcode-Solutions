class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
      # Initialize a counter to track how many bits we shift
      count = 0

# Keep shifting m and n to the right until they become equal
# This helps find the common prefix (highest bits that are the same)
      while (m < n):
        m = m >> 1  # Right shift m by 1 (equivalent to floor divide by 2)
        n = n >> 1  # Right shift n by 1
        count += 1  # Increment shift count

# After loop, m == n and contains the common prefix
# Shift m back to the left to restore the original magnitude
      return m << count  # Fill in the trailing zero bits with left shift
