# 🔐 MyPass

A simple desktop password manager built with Python and Tkinter. MyPass lets you generate strong random passwords, save your website logins locally, and search through saved entries for quick reference.

## Features

- **Website / Email / Password entry fields** — quickly log credentials for any site
- **Generate Password button** — creates a strong random password and drops it straight into the password field
- **Add button** — saves the entry to a local `password_data.json` file
- **Search button** — look up a saved entry by website name
- Clean, minimal UI built entirely with Tkinter

## How It Works

**Adding an entry:**
1. Enter the **Website** name
2. Enter the **Email/Username** used for that site
3. Either type your own password or click **Generate Password** to auto-fill a strong one
4. Click **Add** to save the entry

**Searching for an entry:**
1. Enter the **Website** name in the Website field
2. Click **Search**
3. If a matching entry exists, the Email and Password fields will populate with the saved credentials

Each entry is saved in `password_data.json` in the format:

```json
{
    "Website Name": {
        "email": "user@example.com",
        "password": "generated-password"
    }
}
```

## Requirements

- Python 3.x
- Tkinter (included with most Python installations)

## Running the App

```bash
python main.py
```


## Project Structure