def encrypt(message, key):
    encrypted_message = ''.join(
        chr((ord(char) - 97 + key) % 26 + 97) if char.islower() else
        chr((ord(char) - 65 + key) % 26 + 65) if char.isupper() else
        char
        for char in message
    )
    return encrypted_message


if __name__ == "__main__":

    key = int(input("Enter key: "))
    message = input("Enter message: ")
    result = encrypt(message, key)
    print(f"Result: {result}")
