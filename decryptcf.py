def decrypt(obfuscatedEmail):
    output = ""
    xorKey = int(obfuscatedEmail[:2], 16)
    for i in range(2, len(obfuscatedEmail), 2):
        output += chr(int(obfuscatedEmail[i:i+2], 16) ^ xorKey)
    return output


if __name__ == "__main__":
    print(decrypt("6d6f6e6b6579"))
