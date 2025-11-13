print ("welcome to my word game ")

userinput1 = input("name a occupation? ")
userinput2 = input("name a country? ")
userinput3 = input("name a plural noun? ")
userinput4 = input("name a verb? ")
userinput5 = input("name a adjective? ")
userinput6 = input("name a personal item? ")
userinput7 = input("name a holiday? ")
userinput8 = input("what's your name? ")

replacements = [
    ["An occupation", "OCCUPATION"],
    ["A country", "COUNTRY"],
    ["A plural noun", "PLURAL_NOUN"],
    ["A verb, like 'run,' 'eat' or 'think'", 
    "VERB"],
    ["An adjective, like 'friendly,' 'long,' or "
    "'warm'", "ADJECTIVE"],
    ["A personal item", "PERSONAL_ITEM"],
    ["A holiday, like Christmas or labor Day"],
    ["Your name", "NAME"],
]

for replacement in replacements:
    print(replacement)

OCCUPATION = userinput1.replace("OCCUPATION", userinput1)
COUNTRY = userinput2.replace("COUNRTY", userinput2)
PLURAL_NOUN = userinput3.replace("PLURAL_NOUN", userinput3)
VERB = userinput4.replace("VERB", userinput4)
ADJECTIVE = userinput5.replace("ADJECTIVE", userinput5)
PERSONAL_ITEM = userinput6.replace("PERSONAL_ITEM", userinput6)
HOLIDAY = userinput7.replace("HOLIDAY", userinput7)
NAME = userinput8.replace("NAME", userinput8)

proseString = (f'''
Hi mom,

Just writing to tell you that I've quit my job as a {OCCUPATION} and I'm moving to
{COUNTRY}. The truth is, I've always been passionate about {PLURAL_NOUN}, and {COUNTRY}
is the best place in the world to build a career around them. I'll need to start
small-- At first, all I'll be allowed to do is to {VERB} near them, but when people 
see how {ADJECTIVE} I can be, I'm sure to rise to the top. 

Don't worry about me, and tell dad to take good care of my {PERSONAL_ITEM}. I'll be
sure to call every {HOLIDAY}.

Love,

{NAME}
''')

print(proseString)