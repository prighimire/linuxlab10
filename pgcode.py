import sys

def caesar_cipher(key, message):
    message=message
    shift=key
    message = message.upper()

    encoded_message = ""
    for letter in message:
        if letter.isalpha():
            encoded_letter = chr(((ord(letter) - 65 + shift) % 26) + 65)
            encoded_message += encoded_letter

    block_size = 5
    for i in range(0, len(encoded_message), block_size):
        print(encoded_message[i:i+block_size], end=" ")
        if (i+block_size) % (block_size*10) == 0:
            print()

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv)>3:
        print("invalid input")
        sys.exit(1)
    
    key = int(sys.argv[1])
    
    if len(sys.argv) == 3:
        message = sys.argv[2]
    else:
        message = sys.stdin.read()
    
    caesar_cipher(key, message)
    sys.exit(0)