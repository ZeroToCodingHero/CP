
proseString = '''
Hi mom,

Just writing to tell you that I've quit my job as a OCCUPATION and I'm moving to
COUNTRY. The truth is, I've always been passionate about PLURAL_NOUN, and COUNTRY
is the best place in the world to build a career around them. I'll need to start
small-- At first, all I'll be allowed to do is to VERB near them, but when people 
see how ADJECTIVE I can be, I'm sure to rise to the top. 

Don't worry about me, and tell dad to take good care of my PERSONAL_ITEM. I'll be
sure to call every HOLIDAY.

Love,

NAME
'''

questions = [
    ["name an occupation"],
    ["name a country"],
    ["name a plural noun"],
    ["name a verb"],
    ["name an adjective"],
    ["name a personal item"],
    ["name a holiday"],
    ["what's your name?"],
]

userinput = input(questions)

replacements = [
    ["OCCUPATION", userinput],
    ["COUNTRY", userinput],
    ["PLURAL_NOUN", userinput],
    ["VERB", userinput],
    ["ADJECTIVE", userinput],
    ["PERSONAL_ITEM", userinput],
    ["HOLIDAY", userinput],
    ["NAME", userinput],
]

for question in questions:
    userinput = input(questions)
    proseString = proseString.replace(questions, replacements)

print(proseString)

"""
userinput = input("name a occupation? ")
newProseString = newProseString.replace("OCCUPATION", userinput)

userinput = input("name a country?  ")
newProseString = newProseString.replace("COUNTRY", userinput)

userinput = input("name a plural noun?, A plural noun is a noun that refers to more than one 'persons', 'places', 'things', or 'ideas' ")
newProseString = newProseString.replace("PLURAL_NOUN", userinput)

userinput = input("name a verb A verb?, is a word that describes an action, occurrence, or state of being like 'run,' 'eat' or 'think' ")
newProseString = newProseString.replace("VERB", userinput)

userinput = input("name a adjective?, An adjective is a word that modifies or describes a noun or pronoun like 'friendly,' 'long,' or "
    "'warm' ")
newProseString = newProseString.replace("ADJECTIVE", userinput)

userinput = input("name a personal item? like 'wallet', 'keys' or 'tablet' ")
newProseString = newProseString.replace("PERSONAL_ITEM", userinput)

userinput = input("name a holiday A holiday? like Christmas or labor Day ? ")
newProseString = newProseString.replace("HOLIDAY", userinput)

userinput = input("what's your name? ")
newProseString = newProseString.replace("NAME", userinput)
"""






