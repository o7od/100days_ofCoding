# 🔐 MyPass

A simple desktop password manager built with Python and Tkinter. MyPass lets you generate strong random passwords and save your website logins locally for quick reference.

## Features

- **Website / Email / Password entry fields** — quickly log credentials for any site
- **Generate Password button** — creates a strong random password and drops it straight into the password field
- **Add button** — saves the entry to a local `.txt` file
- Clean, minimal UI built entirely with Tkinter

## How It Works

1. Enter the **Website** name
2. Enter the **Email/Username** used for that site
3. Either type your own password or click **Generate Password** to auto-fill a strong one
4. Click **Add** to save the entry

Each entry is appended to a local text file (e.g. `data.txt`) in the format:

```
Website | Email/Username | Password
```

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

## Running the App

```bash
python main.py
```

*(Update the filename above if your main script is named differently.)*

## Project Structure

```
password_manager/
├── main.py          # App entry point / GUI logic
├── data.txt          # Saved credentials (created after first save)
└── README.md
```

## Planned Improvements

- [ ] Search saved entries by website
- [ ] Switch from plain `.txt` storage to JSON for structured data
- [ ] Add basic encryption for stored passwords
- [ ] Input validation (e.g. empty field checks before saving)
- [ ] Copy-to-clipboard button for generated passwords

## Notes

⚠️ Passwords are currently stored in **plain text** in a local file. This project is for learning purposes — avoid using it to store real, sensitive credentials until encryption is added