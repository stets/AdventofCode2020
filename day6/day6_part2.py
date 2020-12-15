# https://adventofcode.com/2020/day/6

answer_list = open("answers.txt", "r").read().split('\n\n')

response_count = 0

for response in answer_list:
    response = response.rstrip()
    
    print('new group')
    group_set = []
    for each in response.split('\n'):
        group_set.append(set(list(each)))

    intersection = set.intersection(*group_set)
    print(intersection)
    print(f"Got back length: {len(intersection)} of intersecting answers")
    response_count += len(intersection)


print(f"Got {response_count} Yes answers to questions")