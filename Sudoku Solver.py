from datetime import datetime
start_time = datetime.now()
grid = [[0, 6, 0, 0, 3, 0, 0, 0, 0],
        [0, 0, 1, 0, 7, 6, 9, 4, 0],
        [0, 8, 0, 9, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 1, 0, 0, 0],
        [0, 2, 8, 0, 9, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 6, 0],
        [7, 0, 0, 8, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 2],
        [0, 9, 0, 0, 1, 0, 3, 0, 0]]

def printgrid(grid):
    count = 1
    print('┍-- - - ┬ - - - ┬ - - --┑')
    for i in range(9):
        print('| ', end='')
        for j in range(9):
            print(grid[i] [j], end=' ')
            if (j + 1) % 3 == 0:
                print('| ', end='')
        print()
        if (i+1) % 3 == 0 and count <= 2:
            print('┝-- - - + - - - + - - --┥')
            count += 1
    print('┕-- - - ┴ - - - ┴ - - --┙')
def possible(grid, r,c,n):
    if n in grid[r]:
        return False
    for i in range(9):
        if n == grid[i] [c]:
            return False
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[(r // 3) * 3 + i][(c // 3) * 3 + j] == n:
                return False
    return True

def solve():
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1,10):
                    if possible(grid, r,c,n):
                        grid[r][c] = n
                        solve()
                        grid[r][c] = 0
                return 
    printgrid(grid)

if __name__ == '__main__':
    solve()
    end_time = datetime.now()
    print(end_time-start_time)
    
