bo = [
    [6,9,2,3,4,5,8,7,1],
    [1,8,5,7,2,6,3,4,0],
    [0,0,7,8,9,0,0,5,6],
    [0,6,0,0,7,0,1,0,0],
    [4,0,3,1,6,2,0,0,8],
    [9,0,1,0,3,0,7,6,4],
    [0,0,0,0,0,3,0,0,7],
    [2,3,0,6,0,0,9,0,0],
    [7,1,0,0,5,4,0,0,3],
]

class sudoku():
    def __init__(self,board):
        self.board = board
        self.solved = False
        self.solve_list = []
        self.pos = ()
        self.incorrect = {}
        self.pos_c = 0
        self.pos_r = 0
        self.solution=0
        print("_ " * 14 + "\n")
        print("Printing Sudoku Board input")
        self.printer()

    def printer(self):
        print("_ "*14+"\n")
        for row in self.board:
            print(row)
        print("_ " * 14+"\n")

    def solved_check(self):
        self.pos = self.find_unsolved()
        if self.pos == None:
            self.solved = True
        else:
            return self.pos

    def find_unsolved(self):
        for x in range(9):
            for y in range(9):
                if self.board[x][y] == 0:
                    if (x,y) not in self.solve_list:
                        self.solve_list.append((x,y))
                    if (x,y) not in self.incorrect:
                        self.incorrect[(x,y)] = []
                    return (x,y)

    def number_tester(self):
        i=1
        while i <= 9:
            if i not in self.incorrect[self.pos]:
                if self.check_row(i):
                    if self.check_col(i):
                        if self.check_grid(i):
                            self.solution = i
                            return self.solution
            i+=1
        else:
            return False

### Check rows
    def check_row(self,num):
        row = self.board[self.pos[0]]
        if num not in row:
            return True
        else:
            return False

### Check columns
    def check_col(self,num):
        col = []
        for r in self.board:
            col.append(r[self.pos[1]])
        for x in range(9):
            if num not in col:
                return True
            else:
                return False

### Check 3x3 grids
    def check_grid(self,num):
        mod_row = self.pos[0] // 3
        mod_col = self.pos[1] //3
        grid_col,grid_row = mod_col*3, mod_row*3
        grid_cols = [row[grid_col:grid_col + 3] for row in self.board]
        grids = grid_cols[grid_row:grid_row+3]
        flat_grid=[]
        for grid in grids:
            for item in grid:
                flat_grid.append(item)
        if num not in flat_grid:
            return True
        else:
            return False

    def adj_board(self):
        self.board[self.pos[0]][self.pos[1]] = self.solution
        #return self.board

    def solve(self):
        while self.solved == False:
            self.solved_check()
            if self.solved == True:
                return self.board
            if self.number_tester()!=False:
                self.adj_board()
            else:
                self.incorrect.pop(self.pos)
                self.solve_list.pop()
                self.pos = self.solve_list[-1]
                x=self.pos[0]
                y=self.pos[1]
                self.incorrect[self.pos].append(self.board[x][y])
                self.board[x][y] = 0
        #return self

a = sudoku(bo)
b=a.solve()
for row in b:
    print(row)
