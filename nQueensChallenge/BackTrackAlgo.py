#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
.. module:: BackTrackAlgo
.. module author:: agarrido
:synopsis: Implementation of backtrack algorithm for Solver class
:note: Based on https://github.com/sol-prog/N-Queens-Puzzle
"""

class BackTrack(object):
    '''
        Generate all valid solutions for the n queens using BackTracking
    '''

    def __init__(self, size):
        """
           Constructor for BackTracking algorithm
        """
        self.size = size
        self.solutions = 0
        self.boards = []

    def solve(self):
        """
        Solve the n queens and return the number of solutions and positions
        """
        if self.size < 1:
            return self.solutions, self.boards #Not possible solutions
        positions = [-1] * self.size
        self.put_queen(positions, 0)
        return self.solutions, self.boards

    def put_queen(self, positions, target_row):
        """
        Try to place a queen on target_row by checking all N possible cases.
        If a valid place is found the function calls itself trying to place a queen
        on the next row until all N queens are placed on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            self.boards.append(positions[:])
            self.solutions += 1
        else:
            # For all N columns positions try to place a queen
            for column in range(self.size):
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    positions[target_row] = column
                    # Here we call the backtring (recursion)
                    self.put_queen(positions, target_row + 1)

    def check_place(self, positions, ocuppied_rows, column):
        """
        Check if a given position is under attack from any of
        the previously placed queens (check column and diagonal positions)
        """
        for i in range(ocuppied_rows):
            if (positions[i] == column
                    or positions[i] - i == column - ocuppied_rows
                    or positions[i] + i == column + ocuppied_rows):
                return False
        return True

    @staticmethod
    def show_full_board(size, positions):
        """Show the full NxN board"""
        for row in range(size):
            line = ""
            for column in range(size):
                if positions[row] == column:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print("\n")


if __name__ == "__main__":
    # run as standalone script
    import sys, traceback
    try:
        if len(sys.argv) < 2:
            print('To few arguments, please specify a board size')
            sys.exit(1)
        size = int(sys.argv[1])
        backTrackObj = BackTrack(size)
        solutions, boards = backTrackObj.solve()
        for position in boards:
            backTrackObj.show_full_board(size,position)
        print("Found", solutions, "solutions.")
        sys.exit(0)
    except KeyboardInterrupt as kie:
        raise kie
    except SystemExit as se:
        raise se
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        sys.exit(1)
