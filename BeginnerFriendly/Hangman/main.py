##### Hangman Project #####
import random;
words = [
    "apple", "bridge", "cloud", "dance", "eagle", "forest", "garden", "harbor",
    "island", "jungle", "kettle", "lantern", "marble", "needle", "ocean", "pencil",
    "quartz", "rabbit", "silver", "tunnel", "umbrella", "violin", "walnut", "xenon",
    "yellow", "zipper", "anchor", "basket", "candle", "diamond", "ember", "falcon",
    "glacier", "hammer", "ivory", "jasmine", "knuckle", "lemon", "mustard", "napkin",
    "oyster", "pepper", "quill", "ribbon", "saddle", "thistle", "urchin", "velvet",
    "willow", "xylem", "yarn", "zephyr", "acorn", "blizzard", "cobalt", "dagger",
    "eclipse", "fern", "granite", "hollow", "inkwell", "jackal", "kelp", "lava",
    "mosaic", "nectarine", "obsidian", "pebble", "quicksand", "raven", "sapphire",
    "thorn", "umber", "vortex", "weasel", "yolk", "zenith", "amber", "boulder",
    "crimson", "dusk", "enigma", "flint", "gravel", "heron", "indigo", "jade",
    "kestrel", "larch", "mango", "nebula", "olive", "prism", "quest", "rust",
    "slate", "timber"
]

## Method that checks the given letter against the letters in the word
def checkInput(guess, word):
    for i in range(len(word)):
        if word[i] == guess:
            randomWordOnDisplay[i] = guess
            return True
    return False

### Variables
word = random.choice(words)
randomWord = list(word)
countLives = 6

## Word To Guess
print("Word to guess: ", end="")

randomWordOnDisplay = []
for i in range(len(randomWord)):
    randomWordOnDisplay.append("_")
    print("_", end="")

print()


## Taking input
while True:
    guessedLetter = str(input("Guess a letter: "))  
    if checkInput(guessedLetter, randomWord):
        for char in randomWordOnDisplay:
            print(char, end="")
        if randomWordOnDisplay == randomWord:
            print("You win!")
            break
    else:
        countLives -= 1
        print(f"You guessed {guessedLetter}, that's not in the word. You lose a life.")
        if countLives == 0:
            print(f"\n**************************************IT WAS {word}! YOU LOSE**************************************")
            break
    print(f"\n**************************************{countLives}/6 LIVES LEFT**************************************")



        





