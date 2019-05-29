import copy
import sys

# Finding a path and returning its length 
def findPath(i,j,char,visited,currMax):
    if (0 <= i and i < n and 0 <= j and j < m and not visited[i][j]): 
        if matrix[i][j] != char: # If on the current position is a character, different than than the one we started from, we have reached the end of the path from the position
         return currMax
        if matrix[i][j] == char: # If on the current position is the same character, as the one we started from, then we mark the position as visited
            visited[i][j] = True
        return max( findPath(i-1,j,char,copy.deepcopy(visited),currMax+1), 
                    findPath(i+1,j,char,copy.deepcopy(visited),currMax+1), 
                    findPath(i,j-1,char,copy.deepcopy(visited),currMax+1), 
                    findPath(i,j+1,char,copy.deepcopy(visited),currMax+1))
    return 0

# We open every file and read line by line and create a matrix
for i in range(len(sys.argv)-1):
    f = open(sys.argv[i+1])
    
    matrix = []
    
    dimension = f.readline().split(' ')
    n = int(dimension[0])
    m = int(dimension[1])
    
    for i in range(n):
        line = f.readline().replace('\n','').replace(' ','')
        matrix.append(line)
    print(matrix)
    
    f.close()

    maxSequence = 0 # Storing the length of the longest adjacent sequence
    currMax = 0 # Storing the length of the current path

    for i in range(n):
        for j in range(m):
            visited = [[False for j in range(m)] for i in range(n)]
            currMax = findPath(i,j,matrix[i][j],visited,0)
            if (currMax > maxSequence):
                maxSequence = currMax

    print(maxSequence)