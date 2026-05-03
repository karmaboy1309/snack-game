<div align="center">

# 🐍 Terminal Snake

<img src="assets/hero.png" alt="Terminal Snake Hero" width="800"/>

**A classic, single-file, retro Snake game built entirely in Python using the `curses` library.**

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg?style=for-the-badge)](#)

[Features](#-features) • [Installation](#-installation) • [How to Play](#-how-to-play) • [Tech Stack](#-tech-stack) • [Contributing](#-contributing)

</div>

---

## 🎯 Overview

Terminal Snake is a lightweight, dependency-free (on Unix) recreation of the classic arcade Snake game, designed to run right in your terminal. It features dynamic speed scaling, responsive controls, and a minimalist ASCII aesthetic. Whether you're looking for a quick distraction or a clean example of terminal-based game loops in Python, this project delivers.

## ✨ Features

- **Zero External Game Engines**: Built purely with Python's built-in `curses` and `random` libraries.
- **Dynamic Difficulty**: The game progressively speeds up as you consume food and grow longer.
- **Robust Collision Detection**: Handles self-collision and border-collision with immediate game-over states.
- **Non-blocking Input**: Smooth gameplay achieved via `curses` nodelay handling.
- **Cross-Platform**: Playable on Linux, macOS, and Windows (via `windows-curses`).

## 🚀 Installation

### Prerequisites
Make sure you have Python 3.x installed on your system.

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/terminal-snake.git
cd terminal-snake
```

### 2. Environment Setup

**For macOS / Linux:**
The `curses` library comes pre-packaged with Python. No additional installation is required!

**For Windows:**
Windows doesn't natively support the `curses` module out of the box. You will need to install the Windows port:
```powershell
python -m pip install windows-curses
```

### 3. Run the Game
```bash
python snake.py
```

## 🎮 How to Play

- **`↑` Up Arrow**: Move Up
- **`↓` Down Arrow**: Move Down
- **`←` Left Arrow**: Move Left
- **`→` Right Arrow**: Move Right

**Objective:** Eat the food (`@`) to grow your snake (`#`). Do not hit the walls or bite your own tail!

## 🛠️ Tech Stack

- **Language:** Python 3
- **Core Library:** `curses` (Terminal handling & rendering)
- **Logic:** `random` (Food coordinate generation)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](../../issues) if you want to contribute. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

---
<div align="center">
Made by Darshan Makwana
</div>
