# Default mode for opening the txt files is read
# with open("notes.txt") as f:
#     content = f.read()
#     print(content)

# Writing to a file, will delete everything in the notes.txt file and write
# with open("notes.txt", mode="w") as file:
#     file.write("New text")

# writing to a file but keeping the original content intact
# with open("notes.txt", mode="a") as file:
#     file.write("\nNew Text")

# from pathlib import Path
# abs_path = Path("notes.txt").resolve()
# print(abs_path)

with open("../../../../../notes.txt", mode="r") as new_file:
    content = new_file.read()
    print(content)