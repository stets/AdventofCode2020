# https://adventofcode.com/2020/day/6

answer_list = open("answers.txt", "r").read().split('\n\n')

response_count = 0

for response in answer_list:
    answered_yes = set([])
    response = response.rstrip()
    for each in response:
        #print(each)
        answered_yes.add(each)
        answered_yes.discard('\n')
        
    print(answered_yes)
    print(len(answered_yes))
    response_count += len(answered_yes)

print(f"Got {response_count} Yes answers to questions")