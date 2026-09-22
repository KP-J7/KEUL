'''xlib v0.1 (It is a part of KEUL library)'''
import string
import secrets
def create():
    print("Creating...")
    for i in range(3):
        print("......")
    print("Password creating was initialised")
def start():
    print("Generation started")
def generation(length):
    characters = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(characters) for _ in range(length))
        if (any(c.islower() for c in password)     
            and any(c.isupper() for c in password)     
            and sum(c.isdigit() for c in password) >= 2): 
                return password  