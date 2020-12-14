# open the text file 
file = open("password_policy.txt", "r")

validPasswords = 0

for line in file:

    # check the password policy
    line.split(":")
    position_one = int(line.split(":")[0].split(" ")[0].split("-")[0])
    position_two = int(line.split(":")[0].split(" ")[0].split("-")[1])
    character = line.split(":")[0].split(" ")[1]
    
    # parse the password 
    password = line.split(":")[1].strip(" ")
    # count letter occurences in password
    characterCount = password.count(character)

    if password[position_one - 1] == character and password[position_two - 1] == character:
        pass        

    elif password[position_one - 1] == character or password[position_two - 1] == character:
        validPasswords += 1
        print("day 2 advent calendar part two answer: {}".format(validPasswords))

    else:
        pass
