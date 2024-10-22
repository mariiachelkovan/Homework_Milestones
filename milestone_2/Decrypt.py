def decrypt(message, key):
    decrypted_message = ''.join(
        chr((ord(char) - 97 - key) % 26 + 97) if char.islower() else
        chr((ord(char) - 65 - key) % 26 + 65) if char.isupper() else
        char
        for char in message
    )
    return decrypted_message


if __name__ == "__main__":
    key = int(input("Enter key: "))
    message = input("Enter message: ")
    result = decrypt(message, key)
    print(f"Result: {result}")
