"""
permutation
nPr = n! / (n - r)!

nums = [1, 2, 3]

1
  2
    3 => [1, 2, 3]
  3
    2 => [1, 3, 2]
2
  1
    3 => [2, 1, 3]
  3
    1 => [2, 3, 1]
3
  1
    2 => [3, 1, 2]
  2
    1 => [3, 2, 1]
"""


def permute(nums):
    """
    0(n!) time
    0(n^2) space
    """
    permutations = []

    def dfs(picked, unpicked):
        if not unpicked:
            return permutations.append(picked)
        for i, num in enumerate(unpicked):
            dfs(picked + [num], unpicked[:i] + unpicked[i + 1 :])

    dfs([], nums)

    print(permutations)
    return permutations


permute([1, 5, 6])
