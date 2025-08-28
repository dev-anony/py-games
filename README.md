# py-games

A collection of **classic and fun console-based games written in Python**.  
This repository contains a collection of simple yet fun Python games built using tkinter and turtle. 


##  Repository Structure

`py-games/

│── Hangman/        # Hangman 

│── Minesweeper/        # Minesweeper game 

│── Pong/             # Pong game 

│── README.md         # Project documentation`


##  Games Included

### 1. Minesweeper

A Python implementation of the classic **Minesweeper puzzle game**.

- Left-click to reveal a cell.
    
- Right-click to place/remove a flag.
    
- The game ends when all mines are correctly flagged or when a mine is clicked.
    

**Features:**

- Adjustable board size and difficulty.
    
- Mines are randomly generated.
    
- Win/Loss detection with popup messages.
    

**Run:**

`python minesweeper.py`

---

### 2. Pong

A two-player Pong game built with the `turtle` graphics library.

- Player A controls the left paddle with `W` and `S`.
    
- Player B controls the right paddle with `Up` and `Down`.
    
- Ball bounces off walls and paddles.
    

**Features:**

- Scoreboard displayed at the top.
    
- Game ends after **10 fouls** with a popup showing final score.
    
- Smooth paddle and ball movement.
    

**Run:**

`python pong.py`

---

### 3. Hangman

A word guessing game where you try to guess the hidden word one letter at a time.

**Features:**

- Random word selection from a preset list.
    
- ASCII art for each hangman stage.
    
- Win/Loss detection with final word reveal.
    

**Run:**

`python hangman.py`

---

## Getting Started

### Prerequisites

Make sure you have Python 3 installed. You can check with:

`python --version`

### Clone the Repository

`git clone https://github.com/dev-anony/py-games.git`
`cd python-games`

### Run a Game

`python <game_name>.py`

Example:

`python pong.py`

---

## Learning Concepts Covered

- Event handling in Python (`tkinter`, `turtle`).
    
- Game loops and collision detection.
    
- Random number generation.
    
- Condition checking and state management.
