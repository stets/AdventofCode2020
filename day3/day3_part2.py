file = open("geology.txt", "r")

# go to next line from current - go over 3
# record current "x" position and "y"
# increment x + 1 and increment y + 3
# if above ten, find modulo 10 remainder and use that as index


lines = file.read().splitlines()

#print(lines[1][2])
#x = 0
#y = 0
def find_trees(slope_x, slope_y, x=0, y=0):
    treeCount = 0
    for each in lines:
        #print(str(x) + "," + str(y%31))
        try:
            land_point = lines[x][y%31]
        except IndexError:
            print('hit Index exception lol')
            print("total number of trees: {}".format(treeCount))
            return treeCount
        
        if land_point == '#':
            treeCount += 1 
        
        x += slope_x
        y += slope_y
        
    print("total number of trees: {}".format(treeCount))
    return treeCount


factors = []
slopes = [[1,1], [1,3], [1,5], [1,7], [2,1]]

for x, y in slopes:
    factors.append(find_trees(x,y))

print(factors)
# not 33882624
# 355767552

result = 1 
for each in factors:
    result = result * each
    print(result)