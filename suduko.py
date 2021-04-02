def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c]==0:
                return r,c
    return None,None

def valid(puzzle, guess, row, col):
    r_val=puzzle[row]
    if guess in r_val:
        return False
    c_val=[puzzle[i][col] for i in range(9)]
    if guess in c_val:
        return False
    r_start=(row//3)*3
    c_start=(col//3)*3
    for row in range(r_start,r_start+3):
        for col in range(c_start,c_start+3):
            if guess==puzzle[row][col]:
                return False
    return True

def solve(puzzle):
    r,c=find_next_empty(puzzle)
    if r==None or c==None:
        return True
    for i in range(1,10):
        if valid(puzzle, i, r, c):
            puzzle[r][c]=i
            if solve(puzzle):
                return True
        puzzle[r][c]=0
    return False

puzzle = [
    [3, 9,0,   0, 5, 0,   0, 0, 0],
    [0, 0, 0,   2, 0, 0,   0, 0, 5],
    [0, 0, 0,   7, 1, 9,   0, 8, 0],

    [0, 5, 0,   0, 6, 8,   0, 0, 0],
    [2, 0, 6,   0, 0, 3,   0, 0, 0],
    [0, 0, 0,   0, 0, 0,   0, 0, 4],

    [5, 0, 0,   0, 0, 0,   0, 0, 0],
    [6, 7, 0,   1, 0, 5,   0, 4, 0],
    [1, 0, 9,   0,0, 0,   2, 0, 0]
]
if solve(puzzle):
        print("Solved")
    #pprint(example_board)
        for i in range(9):
            for j in range(9):
                print(puzzle[i][j],end=" ")
            print()
else:
    print("Unsolvable")

  