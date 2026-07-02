#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp




# 1. Reading all the names from the invited_names.txt and adding to a list
with open("Input/Names/invited_names.txt", mode="r") as name_reader:
    names = [name.strip() for name in name_reader.readlines()]


# 2. Getting the starting_letter.txt and 
with open("Input/Letters/starting_letter.txt", mode="r") as letter_reader:
    letter_content = letter_reader.read()
    # individual_letter = letter_content.replace("[name]", "Ozod")

# 3. Creating a new txt file for each invited people
for name in names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as ready_letter:
        individual_letter = letter_content.replace("[name]", name)
        ready_letter.write(individual_letter)
        