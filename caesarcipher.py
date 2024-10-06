def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts text using the Caesar Cipher with a given shift and direction.

    Args:
        text (str): The input text to encrypt or decrypt.
        shift (int): The number of positions to shift the letters (positive for encryption, negative for decryption).
        direction (str): Either "encrypt" or "decrypt".

    Returns:
        str: The encrypted or decrypted text.
    """
    result = ""
    for char in text:
        if char.isalpha():  # Only shift letters, not punctuation or spaces
            ascii_offset = 65 if char.isupper() else 97  # ASCII offset for uppercase or lowercase letters
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            result += char  # Leave non-letter characters unchanged
    return result

def main():
    print("Caesar Cipher Encryptor/Decrypter")
    text = input("Enter the text to encrypt/decrypt: ")
    shift = int(input("Enter the shift value (positive for encryption, negative for decryption): "))
    direction = input("Enter 'encrypt' or 'decrypt': ")

    if direction.lower() == "encrypt":
        encrypted_text = caesar_cipher(text, shift, direction)
        print(f"Encrypted text: {encrypted_text}")
    elif direction.lower() == "decrypt":
        decrypted_text = caesar_cipher(text, -shift, direction)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid direction. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
