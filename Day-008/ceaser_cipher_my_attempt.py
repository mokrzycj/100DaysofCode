alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(word, shift):
    encrypted=""
    for letter in word:
        position=alphabet.index(letter)

        # new_position=position+shift
        # while new_position>len(alphabet):
        #     new_position=new_position-len(alphabet)

        new_position=(position+shift)%len(alphabet)  # more elegant way to restrict position to the length of the alphabet
        encrypted+=alphabet[new_position]
    return encrypted

def decrypt(word, shift):
    decrypted=""
    for letter in word:
        position=alphabet.index(letter)

        new_position=position-shift

        while new_position<0:
            new_position=new_position+len(alphabet)

        decrypted+=alphabet[new_position]
    return decrypted

direction = input("Type 'e' if you want to encrypt a word od 'd' if you want to decrypt one. ")
shift = int(input("How big shift should be? "))

if direction=="e":
    word = input("Type the word you want to encrypt: ")
    print(f"Encrypted word: {encrypt(word, shift)}")
    print(f"Decrypted word: {decrypt(encrypt(word, shift), shift)}")
elif direction=="d":
    word = input("Type the word you want to decrypt: ")
    print(f"Decrypted word: {decrypt(word, shift)}")