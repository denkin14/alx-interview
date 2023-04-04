def island_perimeter(grid):
    perimeter = 0
    
    # iterate over each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            # if the cell is land, add 4 to the perimeter
            if grid[i][j] == 1:
                perimeter += 4
                
                # check if there is land in the adjacent cells and subtract 1 for each adjacent land cell
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < len(grid)-1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < len(grid[0])-1 and grid[i][j+1] == 1:
                    perimeter -= 1
    
    return perimeter

