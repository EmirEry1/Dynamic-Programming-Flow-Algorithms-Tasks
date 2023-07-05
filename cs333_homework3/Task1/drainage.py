
M = []
def findSmallerNeighbor(elevations):
    smallerNeigborsAll = [ [ 0 for i in range(len(elevations)) ] for j in range(len(elevations[0])) ]
    for i in range(len(elevations)):
        for j in range(len(elevations[0])):
            smallerNeighbors = []
            if(i != (len(elevations)-1)):
                if(elevations[i][j] > elevations[i+1][j]):
                    smallerNeighbors.append((i+1,j))
            if(j != (len(elevations[0])-1)):
                if(elevations[i][j] > elevations[i][j+1]):
                    smallerNeighbors.append((i,j+1))
            if(i != 0):
                if(elevations[i][j] > elevations[i-1][j]):
                    smallerNeighbors.append((i-1,j))
            if(j != 0):
                if(elevations[i][j] > elevations[i][j-1]):
                    smallerNeighbors.append((i,j-1))
            smallerNeigborsAll[i][j] = smallerNeighbors
    return smallerNeigborsAll

def CalculateM(smallerNeighborsAll,i,j):
    if M[i][j] != None:
        return M[i][j]
    elif len(smallerNeighborsAll[i][j]) == 0:
        M[i][j] = 1
        return 1
    else:
        max = 0
        for n in range(len(smallerNeighborsAll[i][j])):
            row = smallerNeighborsAll[i][j][n][0]
            column = smallerNeighborsAll[i][j][n][1]
            if max < CalculateM(smallerNeighborsAll,row,column):
                max = CalculateM(smallerNeighborsAll,row, column)
        M[i][j] = max + 1
        return max + 1

def take_input():
    
    file_path = input()
    file = open(file_path, 'r')
    lines = file.readlines()
    
    dimensions = lines[0].split(' ')
    n_rows = int(dimensions[0])
    n_columns = int(dimensions[1])

    elevations = []
    for i in range(n_rows):
        elevations.append(lines[i+1].split(' '))

    for i in range(len(elevations)):
        for j in range(len(elevations[0])):
            elevations[i][j] = int(elevations[i][j])
    
    global M
    M = [ [ None for i in range(len(elevations)) ] for j in range(len(elevations[0])) ]
    smallerNeighborsAll = findSmallerNeighbor(elevations)
    max = 0
    for i in range(len(elevations)):
        for j in range(len(elevations[0])):
            if max < CalculateM(smallerNeighborsAll,i,j):
                max = M[i][j]
    return max
print(take_input())



