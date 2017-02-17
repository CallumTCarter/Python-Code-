# def addTempBlock():
#     global tempBlock
#     # currentPos[0][1] = position(y,x)
#     global currentPos
#     y = currentPos[0]
#     x = currentPos[1]
#     try:
#         if (maze[y+1][x] != 1) and (y+1!= height+1):
#             possibleDirection +=1
#             print 'can move down'
#     except: pass
#     try:
#         if (maze[y-1][x] != 1) and (y-1 != -1):
#             possibleDirection +=1
#             print 'can move up'
#     except: pass
#     try:
#         if (maze[y][x+1] != 1) and (x+1 != width):
#             possibleDirection +=1
#             print 'can move right'
#     except: pass
#     try:
#         if (maze[y][x-1] != 1) and (x-1 != -1):
#             possibleDirection +=1
#             print 'can move left'
#     except: pass
#

def direction():
        global currentPos
        y = currentPos[0]
        x = currentPos[1]
        try:
            if (maze[y+1][x] != 1) and (hasAlreadyBeenVisited([y+1,x]) == False) and (y+1!= height+1):
                return 'down'
        except:
            print 'down is off index'
        try:
            if (maze[y-1][x] != 1) and (hasAlreadyBeenVisited([y-1,x]) == False) and (y-1 != -1):
                return 'up'
        except:
            print 'up is off index'
        try:
            if (maze[y][x+1] != 1) and (hasAlreadyBeenVisited([y,x+1]) == False) and (x+1 != width):
                return 'right'
        except:
            print 'right is off index'
        try:
            if (maze[y][x-1] != 1) and (hasAlreadyBeenVisited([y,x-1]) == False) and (x-1 != -1):
                return 'left'
        except:
            print 'left is off index'


def markLocationAsVisited():
    global currentPos
    global alreadyVisitedLocations

    alreadyVisitedLocations.append(currentPos)

def returnToSavedLocation():
    global currentPos
    global savedLocations


    currentPos = savedLocations[(len(savedLocations)-1)]
    del savedLocations[-1]

def move (x):
    global currentPos
    global previousLocation
    previousLocation = currentPos
    if (x == 'up'):
        currentPos = [(previousLocation[0]-1), (previousLocation[1])]
        print 'moved up'
    if (x == 'right'):
        currentPos = [(previousLocation[0]), (previousLocation[1]+1)]
        print 'moved right'
    if (x == 'down'):
        currentPos = [(previousLocation[0]+1), (previousLocation[1])]
        print 'moved down'
    if (x == 'left'):
        currentPos = [(previousLocation[0]), (previousLocation[1]-1)]
        print 'moved left'
    return

def lookForIntersection ():
    # currentPos[0][1] = position(y,x)
    global currentPos
    possibleDirection = 0
    y = currentPos[0]
    x = currentPos[1]
    try:
        if (maze[y+1][x] != 1) and (hasAlreadyBeenVisited([y+1,x]) == False) and (y+1!= height+1):
            possibleDirection +=1
            print 'can move down'
    except: pass
    try:
        if (maze[y-1][x] != 1) and (hasAlreadyBeenVisited([y-1,x]) == False) and (y-1 != -1):
            possibleDirection +=1
            print 'can move up'
    except: pass
    try:
        if (maze[y][x+1] != 1) and (hasAlreadyBeenVisited([y,x+1]) == False) and (x+1 != width):
            possibleDirection +=1
            print 'can move right'
    except: pass
    try:
        if (maze[y][x-1] != 1) and (hasAlreadyBeenVisited([y,x-1]) == False) and (x-1 != -1):
            possibleDirection +=1
            print 'can move left'
    except: pass

    return (possibleDirection)

def hasAlreadyBeenVisited (nextPos):
    global previousLocation
    global tempBlock

    for location in alreadyVisitedLocations:
        if location == nextPos:
            return True

    if nextPos == previousLocation:
        return True

    for location in tempBlock:
        if location == nextPos:
            return True

    return False


def answer(map):

        #          x
        #        --->
        #    | [0,1,1,0]
        #  y | [0,0,0,1]
        #    v [0,1,0,1]
        #      [1,1,0,0]

        # when doing co-ordinates use (y,x)!

    global alreadyVisitedLocations
    global width
    global height
    global previousLocation
    global currentPos
    global savedLocations
    global steps
    global tempBlock

    # Arrays

    #  -To hold one coord
    previousLocation = [0,0]
    currentPos = [0,0]

    #  -To hold a list of coords
    savedLocations = []
    alreadyVisitedLocations = [[0,0]]
    tempBlock = []

    # Variables
    width = len(map[0])
    height = len(map)
    steps = 0

    print 'while loop starting'
    while (currentPos != [height-1,width-1]) or (len(savedLocations) != 0):
        print lookForIntersection()
        # if your at a dead end
        if (lookForIntersection() == 0):
            print 'DEAD END!'
            print savedLocations
            returnToSavedLocation()
            del tempBlock[:]
        # at an intersection
        if (lookForIntersection() > 1):
            alreadyVisitedLocations.append(previousLocation)
            savedLocations.append(currentPos)
            # addTempBlock()
            move(direction())
            alreadyVisitedLocations.append(currentPos)
            print 'SAVING LOCATION'
            print savedLocations
            print tempBlock
        # one way to go
        if (lookForIntersection() == 1):
            move(direction())
        print currentPos
        steps+=1



    for i in maze:
        print i


    return(steps)


maze = [[0,0,0,0,0],
        [0,1,1,1,1],
        [0,1,0,0,0],
        [0,0,0,1,0]]
print(answer(maze))
