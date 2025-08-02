print("Movie Character Creator")
print("-------------------------"
)
hanging_around = input("Do you like 'hanging around'?: ").lower
print()
gravelly_voice = input("Do you have a 'gravelly' voice?: ").lower
print()
marvelous = input("Do you often feel 'Marvelous'?: ").lower
print()

if hanging_around == "no":
  print("Then you're not Spider-man")
if hanging_around == "yes":
  print("Aha! You're Spider-man! Hi!")
if gravelly_voice == "no":
  print("Aww, then you're not Korg")
if gravelly_voice == "yes":
  print("Aha! You're Korg")
if marvelous == "no":
  print("Aww... then you're not Captain Marvel")
if marvelous == "yes":
  print("Aha! You're Captain Marvel! Hi!")
else:
  print("I don't know who you are")
