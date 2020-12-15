raw_passports = open("passports.txt", "r").read()

passports_list = []
formatted_passports = []

for each in range(raw_passports.count('\n\n') + 1):
    passports_list.append(raw_passports.split('\n\n')[each].replace('\n',' ').split(' '))

    for passport in passports_list:
        new_passport = {}
        for field in passport:
            key = field.split(':')[0]
            value = field.split(':')[1]
            new_passport[key] = value
    formatted_passports.append(new_passport)

    
# 'cid' field is optional
fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

invalidPassports = 0 
for passport in formatted_passports:
    print(passport)
    for each in fields:
        if each not in passport:
            #print("Passport invalid! Missing {} field".format(each))
            #print(passport)
            invalidPassports +=1
            # break out of for if passport invalid
            break
        #elif 'byr' in passport:# and passport.split(' ').split(':'):
            #print(passport.split(' '))
        else:
            pass

# valid is total - invalid
print("{0} invalid passports were found, {1} total passports were given...For a total of {2} valid passports".format(invalidPassports, len(passports_list), len(passports_list)-invalidPassports))

