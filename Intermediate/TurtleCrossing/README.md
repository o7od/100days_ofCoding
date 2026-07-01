# 🐢 Turtle Crossing Game

A classic arcade-style crossing game built with Python's `turtle` module — guide your turtle safely across a busy road full of moving cars to reach the other side!

## 🎮 Gameplay

- Move your turtle from the bottom of the screen to the top, avoiding oncoming traffic.
- Each time you reach the top, you level up and the cars get faster.
- If a car hits your turtle, the game ends.
- Your goal: survive as many levels as possible!

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `↑` (Up Arrow) | Move turtle forward |

## 🛠️ Built With

- Python 3
- [`turtle`](https://docs.python.org/3/library/turtle.html) — graphics and game window
- [`random`](https://docs.python.org/3/library/random.html) — random car spawn timing/position
- [`time`](https://docs.python.org/3/library/time.html) — controlling game speed

## 📂 Project Structure

```
turtle-crossing-game/
├── main.py           # Game loop and core logic
├── player.py         # Player (turtle) class - movement, collision detection
├── car_manager.py     # Handles car creation, movement, and speed increases
├── scoreboard.py      # Tracks and displays level/score
└── README.md
```

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your machine

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/turtle-crossing-game.git
   cd turtle-crossing-game
   ```

2. Run the game:
   ```bash
   python main.py
   ```

No additional dependencies needed — `turtle`, `random`, and `time` are all part of Python's standard library.

## ✅ Features

- [x] Smooth turtle movement using `Screen.listen()` and `onkey()`
- [x] Randomly generated cars with increasing speed per level
- [x] Collision detection between player and cars
- [x] Level tracking and on-screen scoreboard
- [x] Game-over screen when a collision occurs

## 🔮 Future Improvements

- [ ] Add sound effects for collisions and level-ups
- [ ] Add a start menu and restart button
- [ ] Save high scores to a local file
- [ ] Add different car colors/sizes for visual variety

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋 Author

Built by Ozod as part of ongoing Python learning — focused on practicing `turtle` graphics, collision detection, and OOP structure in Python.