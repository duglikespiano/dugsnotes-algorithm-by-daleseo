def encoding(strings):

    # 1. Encoding with a special delimiter
    # 0(n) time | 0(1) space
    # return "😆".join(strings)

    # 2. Encode data with length information
    # 0(n) time | 0(1) space
    text = ""
    for string in strings:
        text += f"{len(string)}:{string}"
    return text


def decoding(strings):
    # 1. Decoding with a special delimiter
    # 0(n) time | 0(1) space
    # return strings.split("😆")

    # 2. Decode data with length information
    # 0(n) time | 0(1) space
    list, start = [], 0
    while start < len(strings):
        mid = strings.find(":", start)
        length = int(strings[start:mid])
        list.append(strings[mid + 1 : mid + 1 + length])
        start = mid + 1 + length
    return list


strings = ["Hello", "World", "Yes:Or:No"]
print(encoding(strings))
print(decoding(encoding(strings)))
