def twoSum(numbers, target):
    # 1
    """
    0(n^2) time
    0(1) space
    """
    # result = []
    # for i in range(len(numbers)):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] + numbers[j] == target:
    #             result.append(i)
    #             result.append(j)
    #             return result
    # return result

    # 2
    """
    0(n) time
    0(n) space
    """
    # store value and indices in a hashtable
    # find target - numbers[i] in the hashtable

    # indices = {}
    # for i, v in enumerate(numbers):
    #     indices[v] = i

    # for i, v in enumerate(numbers):
    #     diff = target - v
    #     if diff in indices and indices[diff] != i:
    #         j = indices[diff]
    #         return [i, j]

    # 3
    """
    0(n) time
    0(n) space
    """
    # store and search the value and indices in the hashtable

    indices = {}

    for i, v in enumerate(numbers):
        diff = target - v
        if diff in indices:
            j = indices[diff]
            return [i, j]
        else:
            indices[v] = i


print(twoSum([11, 15, 2, 7], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
