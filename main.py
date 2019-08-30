import sys
import argparse

from nQueensChallenge.BackTrackAlgo import BackTrack
from nQueensChallenge.SolveNqueens import BackTrackSolver
from nQueensChallenge.db import recreate_database

def _parse_args(args):
    parser = argparse.ArgumentParser()


    parser.add_argument('queens', help='Number of queens to place, default is 8', action="store", type=int, nargs='?' ,default=8)
    parser.add_argument('--no-db', action='store_true', help='Resolve the problem without db persistence')
    parser.add_argument('--clear-db', action='store_true', help='Clear db before running')
    parser.add_argument('--tests', '-t', action='store_true', help='Only run the test suite')
    parser.add_argument('--version', '-v',action='version', version='nQueensChallenge 1.0')

    return parser.parse_args(args)

def main(args=None):
    """Entry point for running the application"""
    args = _parse_args(sys.argv[1:])

    if args.tests:
        print('Running test suite: ')
        import pytest
        pytest.main(["-p","no:warnings", "nQueensChallenge/tests/"])
        #sys.exit(0)

    if args.no_db:
        print('Running without storing results: ')
        backTrackObj = BackTrack(args.queens)
        solutions, boards = backTrackObj.solve()
        for position in boards:
            backTrackObj.show_full_board(args.queens,position)
        print("Found", solutions, "solutions.")
        sys.exit(0)

    if args.clear_db:
        recreate_database()

    print('Resolving puzle with db persistence')
    bs = BackTrackSolver()
    bs.solve_to_n(args.queens)
    sys.exit(0)


if __name__ == "__main__":
    main()
