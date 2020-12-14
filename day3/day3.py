file = open("geology.txt", "r")

# go to next line from current - go over 3
# record current "x" position and "y"
# increment x + 1 and increment y + 3
# if above ten, find modulo 10 remainder and use that as index

treeCount = 0
lines = file.read().splitlines()

#print(lines[1][2])
x = 0
y = 0
for each in lines:
    #print(str(x) + "," + str(y%31))
    land_point = lines[x][y%31]
    #print(land_point)
    if land_point == '#':
        #print(land_point)
        treeCount += 1 
    #print(x, y)
    x += 1
    y += 3
    
print("total number of trees: {}".format(treeCount))