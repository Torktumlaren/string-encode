def encodeString(string):
    encodedString = ""
    for index, character in enumerate(string):
        encodedString += chr(ord(character)+(index % 0x10ffff))

    return encodedString


def decodeString(string):
    decodedString = ""
    for index, character in enumerate(string):
        decodedString += chr(ord(character)-(index % 0x10ffff))

    return decodedString


def main():
    choseEncode = -1
    while choseEncode < 0 or choseEncode > 1:
        choseEncode = 1-int(input("Encode (0) or decode (1): "))  # why

    if choseEncode:
        string = input("String to encode: ")
        print("Encoded: ", encodeString(string))
    else:
        encodedString = input("String to decode: ")
        print("Decoded: ", decodeString(encodedString))


if __name__ == "__main__":
    main()
