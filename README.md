Mastermind

A code-breaking game. Objective is to guess the correct "pegs" (characters) or words. 

With each attempt, you are given the number of correct letters in correct positions, and the number of correct letters. These numbers are given to you in that same order in the game after you type your output.

http://en.wikipedia.org/wiki/Mastermind_%28board_game%29 has a great description of how to play.

This version only supports 4 different pegs.

To play:
In the command line, type "python mastermind.py" for a game with pegs. Type "python mastermind.py file.txt" for a game with words. "File.txt" should have words separated by line, although you can technically play with sentences if you wish.

The game itself has this format (# denotes number):
attempt# yourGuess #correctPositions #correctCharacters

The last 2 numbers might be on a different line, depending on if you pressed "Enter/Return" or ctrl-DD (EOF).

I renamed the pegs to a b c d e f g h as opposed to @ # $ %. You can now play games with more choices of pegs (e.g., 4 peg code can use 6 possible pegs). The choices will go in alphabetical order (if you choose 4 letters, they will be a b c d; if you choose 6 letters, they will be a b c d e f).
