import re

# Daftar email yang akan divalidasi
emails = [
    "my-name@someemail.com",
    "myname@someemail.com",
    "my.name@someemail.com",
    "my.name2019@someemail.com",
    "my.name.2019@someemail.com",
    "somename.201903@someemail.com",
    "my_name.201903@someemail.com",
    "201903myname@someemail.com",
    "201903.myname@someemail.com"
]

# Regex sesuai aturan
pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_]*(\.[a-zA-Z0-9_]+)?@someemail\.com$')

# Validasi
for email in emails:
    if pattern.match(email):
        print(f"{email} --> ✅ PASS")
    else:
        print(f"{email} --> ❌ NOT PASS")

