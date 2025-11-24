🐍🪜 Command Line Snake and Ladder Game
A straightforward, two-player version of the classic Snake and Ladder board game, implemented directly in the Python command line.

This game allows two players to take turns rolling a die and moving their positions, encountering ladders (to climb) and snakes (to slide down), until one player reaches the goal of 100.

📌 Features
Two-Player Gameplay: Designed for Player 1 versus Player 2.

Console-Based Interface: Fully interactive via command line/terminal input.

Automatic Die Roll: Simulates a fair, six-sided die roll (1 to 6).

Snakes and Ladders Logic: Automatically updates the player's position when landing on a special square.

Winning Condition: The first player to land exactly on 100 wins.

Overshoot Rule: Prevents moves that go past 100 (the player's position remains unchanged on an overshoot).

🛠 Technologies Used
Python 3.x

Standard Python Libraries (random module for the die roll).

▶ How to Run the Project
Save the script: Save the provided code as a Python file (e.g., snake_ladder.py).

Open a terminal: Navigate to the folder where you saved the file.

Run the program: Execute the script using Python:
python snake_ladder.py

Play: The game will prompt players to press Enter to roll the die for their turn.
