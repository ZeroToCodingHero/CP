for index, letter in enumerate('abcdefghijklmnopqrstuvwxyz'):
    print(letter + " is the " + str(index +1) + "th letter of the alphabet")

# learn flow control, come back and give these incorrect entries their proper suffix

alphabet = 'abcdefghijklmnopqrstuvwxyz'

lphbt = alphabet # It's 'alphabet' with all of the vowels taken out, get it?
vowels = 'aeiou'

for vowel in vowels:
    lphbt = lphbt.replace(vowel, '')

print(lphbt)

favoriteAlphabet = alphabet
favoriteLetters = 'gsbrox'

for letter in favoriteLetters:
    favoriteAlphabet = favoriteAlphabet.replace(letter, letter.upper())

print(favoriteAlphabet)
