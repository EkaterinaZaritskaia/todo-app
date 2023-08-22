password = input("Enter new password: ")

result = [] #list to record the result of each condition

if len(password) >= 8: #if lenght of a password longer or equal then 8 (1 condition)
    result.append(True) #the first item in a list is going to be True or False
else:
    result.append(False) #if length of password shoter and not equal then 8, so it is False

#Due to the method isdigit(), can't to recognised the number in mixed characters, we used next way:
digit = False #digit - is variable, which is false for now (2 condition)
for i in password: #i - item; interpriter itarate all of the characters of the password (for ex.: first character is 'H' and this is not a digit, so 'digit=True' will not be executed, because 'digit=False')
    if i.isdigit(): #isdigit - determined if a characters is a number or not
        digit = True #if there is a charachter which is a number, so it will be executed 'digit=True'

result.append(digit)

#same with method uppercase():
uppercase = False #(3 condition)
for i in password:
    if i.isupper(): #isupper() - determined if a characters is in upper case or not; upper() - converts the characters to upper case
        uppercase = True

result.append(uppercase)

if all(result): #all - means ' == True'; all - get resulst as a general answer (e.g. not as [True, True, True], but as total: 'True')
    print("Strong Password")
else:
    print("Weak Password")