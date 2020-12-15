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
#fields = ['hgt']

valid_eye_colors = ["amb" , "blu" , "brn" , "gry" , "grn" , "hzl" , "oth"]

def validate_year(min_date, max_date, length, field_value):
    field_value = int(field_value)
    if len(str(field_value)) != 4 or field_value < min_date or field_value > max_date:
        #print(f'year invalid: {field_value}, min {min_date}, max {max_date}')
        return True
    else:
        return False


invalidPassports = 0 
for passport in formatted_passports:
    for field in fields:
        field_value = passport.get(field)
        #print(field_value)
        if field_value == None: 
            #print(field_value)
            invalidPassports += 1
            break
        elif field == 'byr':
            if validate_year(1920, 2002, 4, field_value):
                #print(field_value)
                invalidPassports +=1
                break      
            else:
                pass
        elif field == 'iyr':
            if validate_year(2010, 2020, 4, field_value):
                #print(field_value)
                invalidPassports +=1
                break            
        elif field == 'eyr':
            if validate_year(2020, 2030, 4, field_value):
                #print(field_value)
                invalidPassports +=1
                break
        elif field == 'hgt':
            unit = field_value[-2:].strip()
            if unit != 'cm' and unit != 'in':
                #print(field_value)
                invalidPassports += 1 
                break
            if unit == 'cm':
                cm_value = int(field_value.split('cm')[0])
                if cm_value < 150 or cm_value > 193:
                    #print(field_value)
                    invalidPassports += 1
                    break
            if unit == 'in':
                in_value = int(field_value.split('in')[0])
                if in_value < 59 or in_value > 76:
                    #print(field_value)
                    invalidPassports += 1
                    break

        elif field == 'hcl':
            if field_value[0] != '#':
                #print(field_value)
                invalidPassports +=1
                break
            elif len(field_value[1:]) != 6 or field_value[1:].isalnum() == False:
                #print(field_value)
                invalidPassports +=1
                break
        elif field == 'ecl':
            if field_value not in valid_eye_colors:
                invalidPassports +=1
                break 
        elif field == 'pid':
            if len(field_value) != 9:
                    #print(field_value)
                invalidPassports +=1
                break
            if field_value.isdigit() == False:
                #print(field_value)
                invalidPassports +=1
                break
        else:
            pass

# 253 total pass
print("{0} invalid passports were found, {1} total passports were given...For a total of {2} valid passports".format(invalidPassports, len(passports_list), len(passports_list)-invalidPassports))


# not 86, 88
# Anwer is 103!