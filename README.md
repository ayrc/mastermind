Mastermind

A code-breaking game. Objective is to guess the correct "pegs" (characters) or words. 

With each attempt, you are given the number of correct letters in correct positions, and the number of correct letters. These numbers are given to you in that same order in the game after you type your output.

http://en.wikipedia.org/wiki/Mastermind_%28board_game%29 has a great description of how to play.

This version only supports 4 different pegs.

To play:
In the command line, type "python mastermind.py" for a game with pegs. Type "python mastermind.py file.txt" for a game with words. "File.txt" should have words separated by line, although you can technically play with sentences if you wish.

The game itself has this format (# denotes number):
attempt# yourGuess #correctPositions #correctCharacters

I might add the choice of having a certain number of pegs later (e.g., given 6 possible pegs, decode a 4 peg code).
