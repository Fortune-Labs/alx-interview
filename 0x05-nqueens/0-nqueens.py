#!/usr/bin/python3
"""N Queens"""
import sys


def print_board(board):
    """Format the board for printing"""
    formatted_board = []
    n = len(board)

    for i in range(n):
        formatted_board.append([i, board[i]])

    return formatted_board


def is_position_safe(board, row, col):
    """Check if the position is safe for the queen"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def safe_positions(board, row, n, solutions):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        solutions.append(print_board(board))
        return

    for j in range(n):
        if is_position_safe(board, row, j):
            board[row] = j
            safe_positions(board, row + 1, n, solutions)


def n_queens(n):
    """Main function to solve the N Queens problem"""
    solutions = []
    board = [-1] * n
    safe_positions(board, 0, n, solutions)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = n_queens(n)
    for solution in solutions:
        print(solution)
