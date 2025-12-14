Guess the Word (Mini Hangman) – Python
Project Overview

Guess the Word (Mini Hangman) is a simple command-line game built using Python.
The program randomly selects a word from a file, and the player must guess the word one letter at a time within a limited number of attempts.

This project focuses on core Python concepts such as file handling, loops, conditionals, lists, sets, and user input validation.

Features

Random word selection from an external words.txt file

Letter-by-letter word guessing

Hidden word display using underscores

Reveals all matching letters in correct positions

Input validation:

Only single-letter guesses allowed

Only alphabetical characters accepted

Prevents repeated guesses

Limited number of attempts

Clear win and lose conditions

Clean and beginner-friendly code structure

Project Structure

├── game.py
├── words.txt
└── README.md

How the Game Works

The program loads words from words.txt.

One word is randomly selected as the secret word.

The word is displayed as underscores representing hidden letters.

The player guesses one letter at a time.

If the guessed letter exists in the word, it is revealed in all correct positions.

If the guess is incorrect, the number of remaining attempts decreases.

The game ends when:

The player successfully reveals the entire word, or

The player runs out of attempts.

Requirements

Python 3.x

No external libraries required

How to Run the Program

Make sure Python is installed on your system.

Clone or download the repository.

Ensure words.txt contains one lowercase word per line.

Run the program using:

python main.py

words.txt Format

One word per line

All lowercase letters

No spaces

Example:

python
banana
laptop
coding
logic

Learning Outcomes

Understanding file handling in Python

Using lists and sets effectively

Implementing loops and condition-based logic

Handling and validating user input

Building a complete CLI-based project

Possible Improvements

Add difficulty levels

Add ASCII-based hangman drawing

Track player score

Allow replay without restarting the program

Add timer-based gameplay

Author

Developed by Aryan Sonsurkar