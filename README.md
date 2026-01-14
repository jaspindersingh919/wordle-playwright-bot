🧩 Automated Wordle Solver (Python + Playwright)
📌 Overview

This project is a fully automated Wordle solver that plays the official New York Times Wordle game in a real browser.
It uses Playwright to control Chrome, read live game feedback from the DOM, and applies a constraint-based solver to intelligently guess the correct word within six attempts.

The bot:

Opens Wordle in Chrome

Types guesses like a human

Reads tile feedback (correct, present, absent)

Narrows down possible solutions

Solves the puzzle autonomously

🎯 Key Features

✅ Real browser automation (not an API mock)

✅ Reliable DOM-based feedback extraction using data-state

✅ Shadow DOM traversal (Wordle uses Web Components)

✅ Constraint-based Wordle solving logic

✅ Human-like typing behavior

✅ Clean shutdown after solving

🧠 How It Works (High-Level)
Launch Browser
     ↓
Open Wordle
     ↓
Focus Game Board
     ↓
Make Guess
     ↓
Read Tile Feedback
     ↓
Update Constraints
     ↓
Filter Candidate Words
     ↓
Repeat Until Solved

🗂️ Project Structure
wordle-bot/
│
├── main.py                 # Orchestrates the full game loop
│
├── bot/
│   ├── browser.py          # Browser launch & setup
│   ├── actions.py          # Game interactions (start, focus, type)
│   ├── board_reader.py     # Reads tile feedback from the board
│   └── solver.py           # Wordle solving logic
│
├── words/
│   └── words.txt           # 5-letter word list
│
└── README.md

🧪 Example Output
>>> main() started
Guess 1: aback
Feedback: ['present', 'absent', 'absent', 'absent', 'absent']
Remaining words: 679

Guess 2: daddy
Feedback: ['absent', 'present', 'absent', 'absent', 'absent']
Remaining words: 250

Guess 3: elate
Feedback: ['absent', 'present', 'present', 'present', 'absent']
Remaining words: 3

Guess 4: total
Feedback: ['correct', 'absent', 'absent', 'correct', 'correct']
Remaining words: 1

Guess 5: trial
Feedback: ['correct', 'correct', 'correct', 'correct', 'correct']
SOLVED

🛠️ Technologies Used

Python 3

Playwright (Sync API)

Chromium

DOM & Shadow DOM traversal

Constraint satisfaction algorithms

🔍 Technical Highlights
DOM-Based Feedback Reading

Instead of relying on internal game state, the solver reads Wordle feedback directly from each tile’s:

data-state="correct | present | absent"


This makes the solution robust to UI changes and independent of Wordle’s internal JavaScript.

Solver Logic

The solver maintains:

Fixed letter positions (correct)

Letters that must exist (present)

Letters that must not exist (absent)

Position-specific exclusions for present letters

Each guess tightens constraints and filters the candidate word list.

🚀 How to Run
1. Install dependencies
pip install playwright
playwright install

2. Run the bot
python main.py


Chrome will open visibly so you can watch the bot play.

⚠️ Notes

This project is for educational purposes

It interacts with the live NYT Wordle game

No game logic is reverse-engineered or modified

💼 Resume Description

Built a fully automated Wordle solver using Python and Playwright that interacts with the live NYT Wordle game. Implemented DOM-based feedback extraction, Shadow DOM traversal, and a constraint-based solver to autonomously solve puzzles within standard attempt limits.

📈 Possible Enhancements

Entropy-based guess selection

Headless execution

Batch evaluation across multiple games

Performance statistics (average guesses)

UI overlay or logging dashboard

🏁 Status

✅ Project complete and fully functional