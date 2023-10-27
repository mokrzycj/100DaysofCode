alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(start_text, shift_amount, cipher_direction):
    result=""
    if cipher_direction=="d":
        shift_amount*=(-1)
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            position=(position+shift_amount)%len(alphabet)
            result+=alphabet[position]
        else:
            result+=letter
        
    return result


direction = input("Type 'e' if you want to encrypt a word od 'd' if you want to decrypt one. ")
shift = int(input("How big shift should be? "))
word = input("Type the word you want to encrypt: ")

# print(f"Encrypted word: {ceasar(word, shift, direction)}")
print(f"New word: {ceasar(word, shift, direction)}")