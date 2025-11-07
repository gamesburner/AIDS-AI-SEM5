class Queen_problem:
    def __init__(self):
        self.N=4;

    def printSolution(self, board):
        for i in range(self.N):
            for j in range(self.N):
                print(" " + str(board[i][j]) + " ", end="")
            print()

    def isSafe(self, board, row, col):

        for i in range(col):
            if board[row][i] == 1:
                return False

        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        i = row
        j = col
        while i < self.N and j >= 0:
            if board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True

    def solveNQUtil(self, board, col):

        if col >= self.N:
            return True

        for i in range(self.N):
            if self.isSafe(board, i, col):
                board[i][col] = 1

                if self.solveNQUtil(board, col + 1):
                    return True

                board[i][col] = 0

        return False

    def solveNQ(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        if not self.solveNQUtil(board, 0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True

nQueen = Queen_problem()
nQueen.solveNQ()




