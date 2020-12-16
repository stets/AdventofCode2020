#https://adventofcode.com/2020/day/7
import re
#from IPython import embed

bags = {'bright white': {'shiny gold'}, 'muted yellow': {'shiny gold'}, 'dark orange': {'bright white', 'muted yellow'}, 'light red': {'bright white', 'muted yellow'}}

bags = open("bags.txt", "r").read().split('\n')


bag_mapping = {}

for idx, each in enumerate(bags):
    
    each = each.split('contain')
    
    # get the outtermost bag
    big_bag = bags[idx].split('contain')[0].replace('bags', '').strip()
    # get the contents
    bag_contents = re.sub('\d', '', bags[idx].split('contain')[1]).strip('.').replace('bags','').replace('bag','').split(',')
    bag_contents = [x.replace('\',', '').strip() for x in bag_contents]
    #print(bag_contents)
    #print(big_bag)
    # store the bag_contents in the bag mapping
    bag_mapping[big_bag] = bag_contents


# https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
# add no other as empty so we know to stop
bag_mapping['no other'] = []

# depth first search!
def dfs(visited, bag_mapping, node):
    if node not in visited:
        #if node == 'shiny gold':
        #    print(node)
        visited.add(node)
        for neighbor in bag_mapping[node]:
            dfs(visited, bag_mapping, neighbor)

gold_bags = 0 
for each in bag_mapping:
    visited = set()
    print(f'starting with {each}')
    print(visited)
    dfs(visited, bag_mapping, each)
    if 'shiny gold' in visited:
        print('found a shiny!')
        gold_bags += 1
    print(visited)

# off by one for some reason
print(f'Found {gold_bags - 1} gold bags')
