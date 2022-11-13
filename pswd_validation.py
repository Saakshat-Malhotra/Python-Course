import re
exp = re.compile(r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).*$")
pswd = input("Enter your password: ")

if exp.fullmatch(pswd):
    print("Password is valid")
else:
    print("Password is invalid")
