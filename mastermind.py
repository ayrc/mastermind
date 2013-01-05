#!/usr/bin/python
import random, sys, string, copy

class word_generator:
	def __init__(self, filename):
		f = open(filename, 'r')
		self.lines = f.readlines()
		f.close()

	def chooseline(self):
		line = random.choice(self.lines)
		return line

class peg_generator:
	pegs = ['a','b','c','d','e','f','g','h']
	sequence = []
	def __init__(self,numSlots,numPegs):
		for index in range(numSlots):
			self.sequence.append(random.choice(self.pegs[0:numPegs]))
	def newWord(self,numPegs):
		for index in range(len(self.sequence)):
	        	self.sequence[index] = random.choice(self.pegs[0:numPegs])

def play(codeList):
	trial = 1
	print "Enter your guess:"
	sys.stdout.write(str(trial) + ' ')
	attempt = list(sys.stdin.readline().strip())
	while True:
		numPosRight, numCharRight = 0,0
		for index in range(min(len(codeList),len(attempt))):
			if codeList[index] == attempt[index]:
				numPosRight += 1
		test = copy.deepcopy(codeList)
		for i in range(len(attempt)):
			for j in range(len(test)):
				if attempt[i] == test[j]: 
					del test[j]
					numCharRight += 1
					break
		print ' ' + str(numPosRight) + ' ' + str(numCharRight)
		if attempt == codeList:
			break
		trial += 1
		sys.stdout.write(str(trial) + ' ')
		attempt = list(sys.stdin.readline().strip())
	print "Yay!"
	
def main():
	numGames = None
	while not numGames or numGames < 1:
		try:
			numGames = int(raw_input("How many games do you want to play? "))
			if numGames < 1:
				print "Number of games must be > 0"
		except ValueError:
			print "Invalid number"
	if len(sys.argv) == 2:
		entries = word_generator(sys.argv[1])
		for index in range(numGames):
			print "Round " + str(index+1)
			word = list(entries.chooseline().strip())
			print "There are ", len(word), " characters"
			play(word)
	else:
		codeLen, numChoices = None,None
		while not codeLen or codeLen < 1:
			try:
				codeLen = int(raw_input("Length of code: "))
				if codeLen < 1:
					print "Length must be > 0"
			except ValueError:
				print "Invalid number"
		while not numChoices or numChoices < 1:
			try:
				numChoices = int(raw_input("Number of possible pegs to be used: "))
				if numChoices < 1:
					print "Number of possible pegs must be > 0"
			except ValueError:
				print "Invalid number"
		code = peg_generator(codeLen,numChoices)
		for index in range(numGames):
			print "Round " + str(index+1)
			play(code.sequence)
			code.newWord(numChoices)

if __name__ == "__main__":
	main()
