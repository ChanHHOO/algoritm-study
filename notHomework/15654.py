import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

for permutation in permutations(nums, m):
  for i in range(m):
    print(permutation[i], end=" ")
  print()