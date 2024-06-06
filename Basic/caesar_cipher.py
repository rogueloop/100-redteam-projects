def caesar_cipher(text, shift=3):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char  
    return result

def main():
    print("Caesar Cipher Program")
    print("1. Encode")
    print("2. Decode")
    
    choice = int(input("Enter 1 to encode or 2 to decode: "))
    
    if choice == 1:
        text = input("Enter text to encode: ")
        shift = int(input("Enter Shift count: "))
        encoded_text = caesar_cipher(text,shift)
        print(f"Encoded text: {encoded_text}")
    elif choice == 2:
        text = input("Enter text to decode: ")
        shift = int(input("Enter Shift count: "))
        decoded_text = caesar_cipher(text, -shift)  
        print(f"Decoded text: {decoded_text}")
    else:
        print("Invalid option selected.")

try:
    if __name__ == "__main__":
        main()
except Exception as e:
    print("An unexpected error occurred:", str(e))
    print("Please try again.")
