import re

locations = {"+1": "unitied states and canada", "+62": "indonesia", "+505": "Nicaragua", "+52": "Mexico", "+54": "Argentina", "+55": "Brazil", "+57": "Colombia", "+58": "Venezuela"}

def main():
    pattern = r"(\+\d{1,3}) \d{3}-\d{3}-\d{4}"
    number = input("Number: ")
    
    match = re.search(pattern, number)
    if match:
        country_code = match.group(1)
        print(locations[country_code])
    else:
        print("Invalid")

main()
