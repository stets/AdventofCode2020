import expenses

expenses = expenses.expenses

for expense in expenses:
    for expense2 in expenses:
        for expense3 in expenses:
                
            sum = expense + expense2 + expense3 
            if sum == 2020:
                print("Sum found: {}".format(sum))
                print("Addends are : {0}, {1}, {2}".format(expense, expense2, expense3))
                # 
                print("Day 1 Advent of Code Answer is: {}".format(expense * expense2 * expense3))

        # print the sum of the current index 
        #print(each + each[])

        