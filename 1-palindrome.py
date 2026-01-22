def isPalindrom(string):

    # 1.
    # Loop each character of the string and convert them into lowercase characters
    # Check if the character is an Alphabet or number
    # Check if the converted string is same with the revered, converted string
    # 0(n) time | 0(n) space

    # converted = [character for character in string.lower() if character.isalnum()]
    # return(converted == converted[::-1])

    # 2.
    # Create two variable to point each character of string starts at the beginning and end
    # Loop continues until the two pointers meet
    # Check if the character is an Alphabet or number and ignore it if the character is not alphanumeric
    # Move low forward until it is alphanumeric
    # Move high backward until it is alphanumeric
    # Check if the convereted string is same with the reversed, converted string
    # Move low right, move high left
    # 0(n) time | 0(1) space

    low, high = 0, len(string) - 1
    while low < high:
        while low < high and not string[low].isalnum():
            low += 1
        while low < high and not string[high].isalnum():
            high -= 1
        if string[low].lower() != string[high].lower():
            return False
        low, high = low + 1, high - 1
    return True


print(isPalindrom("A man, a plan, a canal: Panama"))
print(isPalindrom("Race a car"))
print(isPalindrom(" "))
