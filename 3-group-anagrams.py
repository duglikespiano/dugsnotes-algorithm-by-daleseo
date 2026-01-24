def groupAnagrams(strings):

    # 1.
    # Create a dictionary
    # Turn the word into a list of characters
    # Sort characters
    # If this sorted pattern hasn’t been seen before, create a new empty list for it
    # Add the original word to its anagram group
    # Returns all grouped anagrams
    # 0(n * wlog(w))? time | 0(n * w)? space

    # anagrams = {}
    # for word in strings:
    #     sorted_word = str(sorted(word))
    #     if sorted_word not in anagrams:
    #         anagrams[sorted_word] = []
    #     anagrams[sorted_word].append(word)
    # return anagrams.values()

    # 2.
    # Create a dictionary
    # Loop through all n words
    # Creates an array of length 26
    # Loop through each character in the word
    # Runs w times per word (word length)
    # Creates an array of length 26
    # Each index represents a lowercase English letter
    # Each tuple is the signature of the word
    # "eat" → (1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0)
    # "tea" → same tuple ✅

    # 0(n * w)? time | 0(26n)? = 0(n) space
    anagrams = {}
    for word in strings:
        counter = [0] * 26
        for character in word:
            counter[ord(character) - ord("a")] += 1
        if tuple(counter) not in anagrams:
            anagrams[tuple(counter)] = []
        anagrams[tuple(counter)].append(word)
    return anagrams.values()


print(
    groupAnagrams(
        [
            "eat",
            "tea",
            "tan",
            "ate",
            "nat",
            "bat",
        ]
    )
)
