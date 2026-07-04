# NATO Phonetic Alphabet Converter

A simple Python script that converts a user's name into its NATO phonetic alphabet equivalent using `pandas`.

## What it does

1. Reads a CSV file (`nato_phonetic_alphabet.csv`) containing each letter of the alphabet and its corresponding NATO code word (e.g. `A → Alfa`, `B → Bravo`).
2. Builds a dictionary from that data using a dictionary comprehension with `iterrows()`.
3. Takes a name as input from the user.
4. Converts each letter of the name into its phonetic code word and prints the result as a list.

## Example

```
Enter your name: Ben
['Bravo', 'Echo', 'November']
```

## Requirements

- Python 3
- pandas

Install pandas if needed:

```bash
pip install pandas
```

## File structure

```
project/
├── main.py
├── nato_phonetic_alphabet.csv
└── README.md
```

## How to run

```bash
python main.py
```

Then enter your name when prompted.

## Notes

- Input is automatically converted to uppercase, so lowercase and uppercase input both work.
- The `nato_phonetic_alphabet.csv` file must be in the same directory as the script (or the path in `read_csv()` must be updated to match its location).