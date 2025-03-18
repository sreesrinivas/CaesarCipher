def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            # If it's not a letter, don't change it (preserving spaces, punctuation, etc.)
            encrypted_text += char
    
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            decrypted_text += decrypted_char
        else:
            # If it's not a letter, don't change it
            decrypted_text += char
    
    return decrypted_text

def main():
    # Simple choice selection with clear instruction
    choice = input("Enter 'E' to Encrypt or 'D' to Decrypt: ").upper()

    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value (integer): "))
        encrypted_message = caesar_cipher_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")

    elif choice == 'D':
        encrypted_message = input("Enter the encrypted message: ")
        shift = int(input("Enter the shift value (integer): "))
        decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
        print(f"Decrypted Message: {decrypted_message}")

    else:
        print("Invalid choice! Please enter 'E' to encrypt or 'D' to decrypt.")

if __name__ == "__main__":
    main()