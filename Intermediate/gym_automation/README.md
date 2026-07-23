# Gym Class Auto-Booker 🏋️

A Selenium-based automation script that logs into a gym's class booking portal, finds classes on specified days/times, books or joins the waitlist automatically, and then verifies the bookings actually went through.

## What It Does

1. **Logs in** to the gym's website using credentials stored in a `.env` file.
2. **Scans the schedule page** for all class cards, grouped by day.
3. **Filters classes** to only those on target days (default: Tuesday & Thursday) at 6:00 PM.
4. **Books each matching class**:
   - If already booked → counts it and moves on.
   - If already waitlisted → counts it and moves on.
   - If a waitlist spot is available → joins the waitlist.
   - Otherwise → books the class directly.
5. **Retries automatically** on timeouts or intercepted clicks (e.g. when a sticky nav bar blocks a button).
6. **Prints a booking summary** (new bookings, new waitlist entries, already-booked count).
7. **Verifies the results** by navigating to the "My Bookings" page and cross-checking that the expected number of Tue/Thu 6:00 PM classes actually appear there.

## Requirements

- Python 3.9+
- Google Chrome + matching ChromeDriver (handled automatically by Selenium 4.6+)
- Packages:
  ```bash
  pip install selenium python-dotenv
  ```

## Setup

1. Clone or download this project.
2. Create a `.env` file in the project root with:
   ```env
   GYM_URL=https://your-gym-booking-site.com
   EMAIL=your_email@example.com
   PASSWORD=your_password
   ```
3. Run the script:
   ```bash
   python main.py
   ```

On first run, Chrome will open using a persistent profile stored in a local `chrome_profile/` folder (so cookies/sessions can carry over between runs). The browser window stays open after the script finishes (`detach` option) so you can review the results.

## Configuration

Target days and time are currently set near the top of the script:

```python
gym_days = ["Tuesday", "Thursday"]
```

The time filter (`6:00 PM`) is hardcoded inside `book_class()` — update the string match there if you want a different time slot.

## Project Structure

| Function | Purpose |
|---|---|
| `retry()` | Generic retry wrapper — retries a given function on `TimeoutException` or `ElementClickInterceptedException`, up to a set number of attempts. |
| `login()` | Handles the full login flow: clicks the login button, fills in email/password, submits, and waits for the schedule page to load. |
| `book_class()` | Core booking logic — finds class cards, filters by day/time, and books/waitlists/skips based on button state. |
| `get_my_bookings()` | Navigates to the "My Bookings" page and grabs all booking cards for verification. |
| `set_up()` | Configures and launches the Chrome WebDriver with a persistent user profile. |

## Sample Output

```
--------- BOOKING SUMMARY ---------
New Bookings: 1
New waitlists entries: 1
Already booked/waitlisted: 2
Total Tuesday & Thursday 6pm classes: 4

--------- DETAILED CLASS LIST  ---------
 • [New Booking] Spin on (Thursday, Jul 23)
 • [New Waitlist] HIIT on (Tuesday, Jul 28)

-------- Verifying on My Bookings Page --------
✔ Verified: Spin
✔ Verified: HIIT
✔ Verified: Yoga
✔ Verified: Pilates

-------- Verification Result -------
Expected: 4 bookings
Found: 4 bookings
✅ SUCCESS: All bookings verified
```

## Known Limitations / Notes

- Relies on specific CSS class names and element IDs (`class-card-*`, `book-button-*`, etc.) from the gym site's current markup — if the site's frontend changes, selectors may need updating.
- Assumes classes are rendered as visible DOM elements grouped under `day-group-*` containers.
- The waitlist/booking click loop (`while book_button.is_enabled(): ...click()`) assumes the button becomes disabled once the action succeeds; if the site's UI behaves differently, this may need a max-attempt safeguard to avoid looping indefinitely.

## Disclaimer

This script automates interactions with a third-party website. Make sure this complies with the gym's terms of service before running it regularly, and use responsibly (avoid excessive request rates).