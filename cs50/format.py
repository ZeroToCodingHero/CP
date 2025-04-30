import re 

name = input("Enter your name? ").strip().lower()
re.search(r"^(.+), (.+)$", name, re.IGNORECASE)
if matches:
    last, first = matches.groups()
    name = f"{first.strip()} {last.strip()}"
print(f"hello, {name}")




# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first.strip()} {last.strip()}"   
         
# print(f"hello, {name}")
