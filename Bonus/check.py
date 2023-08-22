password = input("Enter a new password: ")

result = []

if len(password) > 7:
    result.append(True)
    print("Great password there!")

else:
    print("Your password is weak.")