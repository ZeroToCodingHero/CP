import re

url = input("URL: ").strip().lower()

if matches := re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))



# username = url.removeprefix("https://twitter.com/", "")
# print(f"Username: {username}")
