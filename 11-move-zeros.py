def moveZeros(numbers):
    # 1
    """
    time: 0(n^2)
    space: 0(1)
    """
    # for i in range(len(numbers)):
    #     if numbers[i] == 0:
    #         for j in range(i + 1, len(numbers)):
    #             if numbers[j] != 0:
    #                 numbers[i], numbers[j] = numbers[j], numbers[i]
    #                 break
    # return numbers

    # 2
    """
    time: 0(n)
    space: 0(n)
    """
    # zeros = []
    # non_zeros = []
    # for number in numbers:
    #     if number == 0:
    #         zeros.append(number)
    #     else:
    #         non_zeros.append(number)
    # return non_zeros + zeros

    # 3
    """
    time: 0(n)
    space: 0(1)
    """
    z = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[i], numbers[z] = numbers[z], numbers[i]
            z += 1
    return numbers


print(moveZeros([0, 1, 65, 0, 4, 0, 1]))
