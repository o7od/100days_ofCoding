import pandas

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_alphabet = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
 
        
def generate_phonetic():
    name = str(input("Enter your name: ")).upper()
    try:
        result = [nato_alphabet[letter] for letter in name]
    except KeyError:
        print("Sorry, only letters in the alphabet please. ")
        generate_phonetic()
    else:   
        print(result)

generate_phonetic()

