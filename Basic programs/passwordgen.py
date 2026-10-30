import string
import random
characters = string.ascii_letters + string.digits + string.punctuation
print("Password Generated")
password = ''.join(random.choice(characters) for _ in range(12))
print(password)
