def twoSum(numbers, target):
    # 1. Binary search
    """
    time : 0(nlog(n))
    space: 0(1)
    """
    # Fix one number first
    # Search for target - current number using binary search
    # If numbers[mid] < complement, move low up
    # If numbers[mid] > complement, move high down
    # If numbers[mid] == complement, return [i, mid]
    #
    # for i in range(len(numbers) - 1):
    #     complement = target - numbers[i]
    #     low, high = i + 1, len(numbers) - 1
    #     while low <= high:
    #         mid = (low + high) // 2  # '//' performs floor division
    #         if numbers[mid] < complement:
    #             low = mid + 1
    #         elif numbers[mid] > complement:
    #             high = mid - 1
    #         else:
    #             return [i, mid]

    # 2. two pointers
    """
    time : 0(n)
    space: 0(1)
    """
    # If sum of 'low' and 'high' is bigger than target, move 'up' an index down
    # If sum of 'low' and 'high' is smaller than target, move 'low' an index up
    # If sum of 'low' and 'high' is same with target,  return [low, high]
    #
    low, high = 0, len(numbers) - 1
    while low < high:
        total = numbers[low] + numbers[high]
        if total < target:
            low += 1
        elif total > target:
            high -= 1
        else:
            return [low, high]


print(twoSum([1, 2, 4, 6, 7, 9, 10, 11, 12], 9))
