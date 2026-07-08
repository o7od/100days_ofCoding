#FileNotFound Error

# try:
#     file = open("file.txt")
#     dict = {"key": "value"}
#     print(dict["key"])
# except FileNotFoundError:
#     file = open("file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} doesn't exist! ")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("throwing an error")



height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouldn't be more over 3 meters")

bmi = weight / height ** 2

print(bmi)

