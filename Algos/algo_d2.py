def checkAround(grid, r, c): #grid 1 1
    grid[r][c] = '0'
    compass = [
        (r-1, c), # 0, 1
        (r, c+1), # 1, 2
        (r, c-1), # 1, 0
        (r+1, c), # 2, 1
    ]
    counter = 0
    for row, col in compass:
        if row >= 0 and col >= 0 and row < len(grid[row]) and col < len(grid) and grid[row][col] == '1':
            counter+=1
            print(row, col)
            counter = checkAround(grid, row, col)
    return counter

def numIslands(grid):
    island = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            counter = checkAround(grid, r, c)
            print("the counter is: ", counter)
            if counter > 0:
                island += 1
    print("Grid: ", grid)
    return island


grid = [
      ["1","1","1","1","0"],      
      ["1","1","0","1","0"],      
      ["1","1","0","0","0"],     
      ["0","0","0","1","1"]]

print(numIslands(grid))

# if  value of the cord = 1  then thats would indicate an island
# cord = 1 counter is add +1  if cord = 0  sub -1 to counter

def checkAround(grid, r, c): #grid 1 1
    grid[r][c] = '0'
    compass = [
        (r-1, c), # 0, 1
        (r, c+1), # 1, 2
        (r, c-1), # 1, 0
        (r+1, c), # 2, 1
    ]
    for row, col in compass:
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[row]) and grid[row][col] == '1':
            checkAround(grid, row, col)

def numIslands(grid):
    island = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == '1':
                island += 1
                checkAround(grid, r, c)
    return island


grid = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],      
      ["1","1","0","0","0"],     
      ["0","0","0","1","1"],
      ["1","0","0","1","1"]]

print(numIslands(grid))