from morse import MORSE_CODE_DICT
text = input("Give me a word to convert into morse code: ").upper()

print(text)
string = ""
for letter in text:
    string = string + MORSE_CODE_DICT[letter] + " "

print(string)
