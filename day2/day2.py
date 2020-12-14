# open the text file 
file = open("password_policy.txt", "r")

validPasswords = 0

for line in file:
    # check the password policy
    line.split(":")
    minimum = int(line.split(":")[0].split(" ")[0].split("-")[0])
    maximum = int(line.split(":")[0].split(" ")[0].split("-")[1])
    character = line.split(":")[0].split(" ")[1]
    
    # parse the password 
    password = line.split(":")[1].strip(" ")
    # count letter occurences in password
    characterCount = password.count(character)

    if characterCount >= minimum and characterCount <= maximum:
        validPasswords += 1
        print("day 2 advent calendar answer: {}".format(validPasswords))

    else:
        pass
