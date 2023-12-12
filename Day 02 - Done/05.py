given_sentence = "The day has been long"

given_sentence = given_sentence[:4] + given_sentence[5:]

print((given_sentence + ' ') * 4)

print((given_sentence + '\n') * 3)

given_sentence = given_sentence[:7] + 'A' + given_sentence[8:]

print(given_sentence[4:16])

print("* " + given_sentence + " *", "is the final sentence with a length of ", len(given_sentence))
