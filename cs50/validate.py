import re # Validate email address

email = input("What's your email? ").strip().lower()

if re.search(r"^\w+@(\w\+\.)?\w+\.(com|edu$", email, re.IGNORECASE):
    print("Vaild")
else:
    print("Invaild")
    
