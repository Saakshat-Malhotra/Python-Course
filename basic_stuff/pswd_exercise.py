username = input("What is your username: ")
password = input("What is your password: ")
pswd_length = len(password)
password1 = "*" * pswd_length
print(f"Hey {username}, your password {password1} is {pswd_length} letters long.")