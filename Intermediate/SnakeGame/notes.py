##### List Inheritance and List Slicing #####

piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# from 2nd index till the end
print(piano_keys[2:])

# Get all elements in the list
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a[::])
print(a[:])

# everything until position 5
print(piano_keys[:5])

## Getting every second item
print(piano_keys[::2])

## Reversing the list
print(piano_keys[::-1])

## Works on tuple too
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:5])