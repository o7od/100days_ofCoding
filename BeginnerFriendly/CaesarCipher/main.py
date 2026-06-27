#################### Function Parameters and Caesar Cipher ####################

## Original alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


## encrypt function that encryptes the given message
def encrypt(original_text, shift_amount):
    ## encode
    msg = [char for char in original_text] ## msg is a list
    ## Encoding Algorithm
    new_word = ""
    for letter in msg:
        if letter in alphabet:
            letter_index = alphabet.index(letter)
            new_let_index = (letter_index + shift_amount) % len(alphabet)
            new_word += alphabet[new_let_index]
        else:
            new_word += letter

    print(f"Your encoded word is {new_word}")

## decrypt algorithm
def decrypt(original_text, shift_amount):
    decoded = [char for char in original_text]
    decoded_word = ""
    for letter in decoded:
        if letter in alphabet:
            let_index = alphabet.index(letter)
            old_let_index = (let_index - shift_amount) % len(alphabet)
            decoded_word += alphabet[old_let_index]
        else:
            decoded_word += letter
    
    print(f"Your decoded word is {decoded_word}")

## starting the game
start = input("Type 'yes' to start the game! ").lower()
while start == 'yes':
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if type not in ('encode', 'decode'):
        print("Invalid type")
        continue #this will not read the read the rest of the code in the while loop and starts again

    message = input("Type your message: ").lower()
    shift_num = int(input("Type the shift number: "))

    if type == 'encode':
        encrypt(message, shift_num)
    ## Decoding Algorithm
    elif type == 'decode':
        decrypt(message, shift_num)
    else:
        print("ERROR: You entered a wrong input\n")
    start = input("Type 'yes' if you want to go again. Otherwise type 'no' ").lower()








