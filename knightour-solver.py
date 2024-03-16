class KnightsTour:
    def __init__(self, n):
        self.n = n
        self.board = [[-1 for _ in range(n)] for _ in range(n)] #initalizing the board where all squares have -1 as value
        self.moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
                      (-2, -1), (-1, -2), (1, -2), (2, -1)] # all possible moves that can be done by the knight where the new square will be x+mv_x ,y+mv_y

    def is_valid(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1 #checking that the move is valid (it's within the board + the square isn't visited yet)

    def knight_tour(self, x, y, move_count):
        self.board[x][y] = move_count # Mark the current cell as visited with the move count

        if move_count == self.n * self.n:# If the move count = number of cells on the board, print the solution
            self.print_solution()
            return True

        for dx, dy in self.moves: # Iterate over all possible moves of the knight
            next_x, next_y = x + dx, y + dy # Calculate the next position after making the move
            if self.is_valid(next_x, next_y): # Check if the move is valid
                if self.knight_tour(next_x, next_y, move_count + 1): # Explore the next move recursively 
                    return True

        self.board[x][y] = -1
        return False

    def print_solution(self): # To print the solution
        for row in self.board:
            print(" ".join(str(cell).zfill(2) for cell in row)) #structure the output


if __name__ == "__main__":
    n = 8  # Size of the chessboard
    start_x, start_y = 0, 0  # Starting position of the knight
    kt = KnightsTour(n)
    kt.knight_tour(start_x, start_y, 1)
