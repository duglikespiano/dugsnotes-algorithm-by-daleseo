def containsDuplicate(numbers):
    # ❌
    """
    time: nP2 = 0(n^2)
    space: 0(1)
    """
    # possible but not efficient when the numbers array is extremely big
    # for i in range(len(numbers) - 1):
    #     for j in range(i + 1, len(numbers)):
    #         if numbers[i] == numbers[j]:
    #             return True
    # return False

    # ✅ 1
    """
    time: 0(nlog(n)) + 0(n) = 0(nlog(n))
    space: 0(1)
    """
    # numbers.sort()
    # for i in range(len(numbers) - 1):
    #     if numbers[i] == numbers[i + 1]:
    #         return True
    # return False

    # ✅ 2
    """
    time: 0(n)
    space: 0(n)
    """
    seen = set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False


print(containsDuplicate([1, 3, 4, 5, 6]))
print(containsDuplicate([1, 3, 6, 4, 5, 6]))
