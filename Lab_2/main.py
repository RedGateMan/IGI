import re

while (True):
	try:
		command = input("1) File Input\n2) Standard input\n")
		break
	except NameError:
		print("Psssst! Choose one of the given options!")

match command.split():
	case ["1"]:
		try:
			inputFile = open("text", "r")
			inputText = inputFile.read()
			inputFile.close()
			print(inputText)
		except FileNotFoundError:
			print("No such file!")
	case ["2"]:
		inputText = input("Enter your text here!\n")

declarativeSentencesAmount = len(re.findall(r"[.]+", inputText))
nonDeclarativeSentencesAmount = len(re.findall(r"[?!]+", inputText))
wordsAmount = len(re.findall(r'\w+', inputText)) - len(re.findall(r'\b\d+\b', inputText))
sentencesLength = 0
wordsLength = 0

print("Declarative: ", declarativeSentencesAmount)
print("Non-declarative: ", nonDeclarativeSentencesAmount)
print("Words: ", wordsAmount)
