def isAnagram(string1, string2):

    # 1.
    # Convert characters of two strings into lower case and sort them
    # Check if sorted strings are same
    # 0(nlog(n)) time | 0(1) space

    # return sorted(string1.lower()) == sorted(string2.lower())

    # 2.
    # Convert characters in strings into lowercase
    # Create counter to put characters
    # Loop strings
    # If the character of string exists in counter, add 1
    # If the character of string does not exist in counter, initialize the character with 1
    # Once check of the first string is done, second string needs to be checked as well
    # If the character of string2 exists in counter, subtract 1
    # If the character of string2 does not exist, just return False as it means the strings are not anagram
    # Return if the counter is empyty after looping two strings

    # 0(n)? time | 0(n)? space
    string1 = string1.lower()
    string2 = string2.lower()
    counter = {}
    for character in string1:
        if character not in counter:
            counter[character] = 0
        counter[character] += 1
    for character in string2:
        if character not in counter:
            return False
        counter[character] -= 1
        if counter[character] == 0:
            del counter[character]
    return not counter


print(isAnagram("anagram", "Nagaram"))
