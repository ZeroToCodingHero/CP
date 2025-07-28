print ("welcome to my word game ")

userinput1 = input("name a occupation? ")
userinput2 = input("name a country? ")
userinput3 = input("name a plural noun? ")
userinput4 = input("name a verb? ")
userinput5 = input("name a adjective? ")
userinput6 = input("name a personal item? ")
userinput7 = input("name a holiday? ")
userinput8 = input("what's your name? ")

occupation = userinput1.replace("OCCUPATION", userinput1)
country = userinput2.replace("COUNRTY", userinput2)
plural_noun = userinput3.replace("PLURAL_NOUN", userinput3)
verb = userinput4.replace("VERB", userinput4)
adjective = userinput5.replace("ADJECTIVE", userinput5)
personal_item = userinput6.replace("PERSONAL_ITEM", userinput6)
holiday = userinput7.replace("HOLIDAY", userinput7)
name = userinput8.replace("NAME", userinput8)

proseString = (f'''
Hi mom,

Just writing to tell you that I've quit my job as a {occupation} and I'm moving to
{country}. The truth is, I've always been passionate about {plural_noun}, and {country}
is the best place in the world to build a career around them. I'll need to start
small-- At first, all I'll be allowed to do is to {verb} near them, but when people 
see how {adjective} I can be, I'm sure to rise to the top. 

Don't worry about me, and tell dad to take good care of my {personal_item}. I'll be
sure to call every {holiday}.

Love,

{name}
''')

print(proseString)

