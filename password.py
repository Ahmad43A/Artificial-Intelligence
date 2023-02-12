username = input("Enter your username: ")
password = input("Enter your password: ")

if password.lower() == "abc$123":
    print("Welcome!")
else:
    print("I don't know you.")
