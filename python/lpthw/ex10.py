# Escape Sequences
tabby_cat = "\tI'm tabbed in."  # \t tabs the text
persian_cat = "I'm split\non a line."  # \n puts it on a new line
backslash_cat = 'I\'m \\ a \\ cat.'  # \\ = \

# ''' lets you write as it's shown '''
fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print("The is a tabby cat {}".format(tabby_cat))
