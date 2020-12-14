import expenses

expenses = expenses.expenses

# find the two entries that sum to 2020 and then multiply those two numbers together.

#1993, 1715, 1997, 1666, ...

for expense in expenses:
    for expense2 in expenses:
        sum = expense + expense2 
        if sum == 2020:
            print("Sum found: {}".format(sum))
            print("Addends are : {0}, {1}".format(expense, expense2))
            print("Day 1 Advent of Code Answer is: {}".format(expense * expense2))