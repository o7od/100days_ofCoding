# Pomodoro Timer

A desktop Pomodoro productivity timer built with Python and Tkinter. It alternates between focused work sessions and breaks, helping you stay productive using the Pomodoro Technique.

## Features

- **Work/Break Countdown** — Automatically counts down work sessions and switches to break periods when time runs out.
- **Session Tracking with Checkmarks** — A ✓ is added after each completed work session, giving a visual record of progress throughout the day.
- **Long Break Cycle** — After every 4 completed work sessions, the app triggers an extended break instead of a short one, following the standard Pomodoro rhythm.
- **Start & Reset Controls** — Start a session whenever you're ready, or reset the timer and progress back to zero at any point.

## How It Works

1. Press **Start** to begin a work session.
2. The countdown timer displays the remaining time and updates every second.
3. When the work session ends, a checkmark (✓) is added to track progress, and a short break automatically begins.
4. This cycle repeats — after 4 work sessions, a longer break is triggered instead of a short one.
5. Press **Reset** at any time to stop the current timer and clear session progress.

## Built With

- **Python** — core application logic
- **Tkinter** — GUI framework for the window, timer display, labels, and buttons

## Why Pomodoro?

The Pomodoro Technique breaks work into focused intervals (traditionally 25 minutes) separated by short breaks, with a longer break after a set number of intervals. This app automates that cycle so you can focus on the work itself rather than tracking time manually.