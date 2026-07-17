# Flight Deals Finder ✈️

A Python automation tool that searches for cheap flight deals from a given departure city, logs the results to a Google Sheet, and sends an SMS alert when it finds the lowest price.

## How It Works

1. **You enter a departure city** when running the script.
2. The city name is converted to its IATA airport code.
3. **SerpApi's Google Flights Deals engine** is queried for flight deals departing from that airport over the next 6 months.
4. The script compares all returned deals and picks out the **cheapest one**.
5. That deal is **posted to a Google Sheet** via the Sheety API.
6. An **SMS alert** is sent via the Vonage Messages API with the destination, price, and outbound date.

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Entry point — orchestrates the search, sheet update, and SMS alert |
| `flights_finder.py` | Queries SerpApi's Google Flights Deals engine |
| `Sheety.py` | Reads/writes flight price data to a Google Sheet via Sheety |
| `send_information.py` | Sends the SMS alert via Vonage |
| `IATA_code.py` | Maps city names to IATA airport codes *(required — not included in this repo yet)* |

## Setup

### 1. Clone and install dependencies

```bash
pip install requests requests_cache python-dotenv vonage
```

### 2. Create a `.env` file

This project keeps all API credentials out of the codebase. Create a `.env` file in the project root with the following variables:

```env
SERP_API=your_serpapi_key
SHEETY_API=your_sheety_endpoint_url
SHEETY_TOKEN=your_sheety_auth_token
VONAGE_API_KEY=your_vonage_api_key
VONAGE_API_SECRET=your_vonage_api_secret
VONAGE_NUMBER=your_vonage_sender_number
VONAGE_TO_NUMBER=your_recipient_phone_number
```

> `.env` is already excluded via `.gitignore` — never commit real API keys.

### 3. Set up your accounts

- **[SerpApi](https://serpapi.com/)** — used to query Google Flights deals data
- **[Sheety](https://sheety.co/)** — turns a Google Sheet into a REST API for storing flight prices
- **[Vonage](https://www.vonage.com/communications-apis/)** — sends the SMS notification

## Usage

Run the script and enter your departure city when prompted:

```bash
python main.py
```

Example:
```
Which city are you flying from? London
Source: API
Successfully added a new travel destination!
```

If a cheaper deal is found, you'll receive an SMS with the destination, price, and outbound date.

## Notes

- API responses for flight and sheet data are cached locally (`requests_cache`) to avoid hitting rate limits on repeated runs.
- `IATA_code.py` (the `city_to_iata` dictionary) is a required dependency for `main.py` but isn't included yet — it should map full city names to their airport codes.

## Possible Improvements

- [ ] Add error handling for cities not found in `city_to_iata`
- [ ] Support multiple departure/destination pairs in one run
- [ ] Schedule the script to run automatically (e.g. via GitHub Actions or cron)