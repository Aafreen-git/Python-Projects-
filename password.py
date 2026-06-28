import random
import string

length = int(input("How long password you want (4,6,8,12 digits)?: "))

class PasswordGenerator:
    def __init__(self):
        self.characters = string.ascii_letters + string.digits + string.punctuation
    
    def generate(self, length):
        password = ""
        for _ in range(length):
            password += random.choice(self.characters)
        return password 

    def save(self, password):
        with open("password.txt", "a") as file:
            file.write(password +"\n")

gen = PasswordGenerator()
password = gen.generate(length)
print(password)

choice = input("Save it? (yes/no): ")
if choice == "yes":
    gen.save(password)
    print("Password Saved!")

