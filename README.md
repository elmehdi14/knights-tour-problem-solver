# Knights Tour Problem Solver
This Python code provides a solution to the Knight's Tour problem. Given a chessboard of size `n x n`, the code finds a sequence of moves for a knight such that the knight visits every square exactly once.

## How it Works
The code implements a depth-first search algorithm to explore all possible knight moves recursively until a valid solution is found. It utilizes backtracking to undo moves that lead to dead ends.

## Usage
1. **Input**: The size of the chessboard (`n`) and the starting position of the knight (`start_x`, `start_y`) can be configured in the `__main__` section.
2. **Output**: Once a solution is found, the code prints the knight's tour on the chessboard.

## Credits
This solution is inspired by the code available [here](https://www.quora.com/How-do-you-write-a-code-using-Python-for-a-Knights-tour-problem).
