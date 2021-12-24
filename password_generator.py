from random import randint

print("PASSWORD GENERATOR\n==================\n")

bounds = [33, 126]
passwords = []
file_name = "passwords.txt"

try:
    number = int(input("How many passwords would you like? "))
    length = int(input("How long would you like the passwords to be? "))

    for i in range(number):
        password = ""
        for j in range(length):
            char = chr(randint(bounds[0], bounds[1]))
            password += char
        passwords.append(password)
    
    file = open(file_name, "w", encoding = "utf-8")
    for p in passwords:
        file.write(p + "\n")
    file.close()
    print("Your passwords have been written to: " + file_name)
        
except Exception as error:
    print("Something went wrong:", error)