
"""
Implement a basic 3x3 box Sudoku solver.

T. R. Whitcomb
21 April 2009
Seat 2A, Alaska Air Flight 667

"""
import itertools
import sys

import numpy as np

NOT_COMPLETED = 0
BOX_SIZE      = 3
PUZZLE_SIZE   = 9

class PuzzleSet(object):
    """
    A collection of Sudoku puzzles.
    """

    def __init__(self):
        self.puzzles = []

    def read(self, filename=None, fileobj=None):
        """Read a set of puzzles out of a file."""
        if fileobj is not None:
            f             = fileobj
            need_to_close = False
        elif filename is not None:
            f             = open(filename, 'r')
            need_to_close = True

        while True:
            new_puzzle = Puzzle()
            try:
                f.next()    # Skip "Grid XX"
                new_puzzle.read(fileobj=f)
            except StopIteration:
                break
            self.puzzles.append(new_puzzle)
        if need_to_close:
            f.close()

    def __iter__(self):
        for puzzle in self.puzzles:
            yield puzzle
        
class Puzzle(object):
    """
    Define a Sudoku puzzle.  The goal of the puzzle is to produce a 3x3 set of
    3x3 squares, with each square ("box"), each row, and each column containing
    the digits 1-9.

    """
    def __init__(self, puzzle_file=None):
        if puzzle_file is not None:
            self.read(puzzle_file)
    
    def read(self, filename=None, fileobj=None):
        """
        Read a Sudoku puzzle in from a file.  This assumes that the puzzle
        is digitized so each row is on a separate line, and each number is
        separated by spaces.  Empty values (i.e. values that we'll need to 
        solve for) are indicated by the NOT_COMPLETED value given above.

        """
        if fileobj is not None:
            f = fileobj
            need_to_close = False
        elif filename is not None:
            f = open(filename, 'r')
            need_to_close = True
        self.solution = self._read(f)
        if need_to_close:
            f.close()

    def solve(self):
        """
        Run the Sudoku solver.  This uses the initial state read in from
        the definition file earlier and iterates until a solution is 
        determined.

        """
        previous_values = np.empty(self.solution.shape, dtype=np.object)
        previous_values[:,:] = None

        iter_count = 0
        while self._solution_is_incomplete():
            iter_count += 1
            solution_domain = itertools.product(range(PUZZLE_SIZE), 
                                                range(PUZZLE_SIZE))
            for (row, column) in solution_domain:
                if self._need_solution(row, column):
                    last_guess = previous_values[row, column]
                    new_guess  = self._enumerate_solutions(row, column,
                                                           last_guess)
                    if len(new_guess) == 1:
                        # Found one!
                        self._add_solution(row, column, new_guess.item())
                    else:
                        previous_values[row, column] = new_guess
            if iter_count % 5 == 0:
                self.print_solution()
        print '(Required %d iterations.)' % iter_count

    def print_solution(self):
        """
        Pretty-print the solution.  This can be used at any state of the
        solution, as entries where a solution has not yet been determined
        will be blanked out.

        """
        self._print_rule()
        for (row_num, row) in enumerate(self.solution):
            self._print_row(row)
            if (row_num+1) % BOX_SIZE == 0:
                self._print_rule()

    def _read(self, file):
        puzzle = []
        lines_read = 0
        while lines_read < 9:
            line = file.next()
            if line.rstrip():
                puzzle.append([int(v) for v in line.rstrip()])
                lines_read += 1
        return np.ma.masked_equal(puzzle, NOT_COMPLETED)

    #------------------------------
    # Iteration control routines
    #------------------------------

    def _solution_is_incomplete(self):
        return np.any(self.solution.mask)

    def _need_solution(self, row, column):
        return self.solution.mask[row, column]

    #------------------------------
    # Constraint check routines
    #------------------------------

    def _is_possible_solution(self, row, column, value):
        return not (self._already_in_row(row, value)       or
                    self._already_in_column(column, value) or
                    self._already_in_box(row, column, value))

    def _already_in_row(self, row, value):
        return value in self.solution[row, :]

    def _already_in_column(self, column, value):
        return value in self.solution[:,column]

    def _already_in_box(self, row, column, value):
        box_row    = int(row / BOX_SIZE)
        box_column = int(column / BOX_SIZE)

        start_row    = BOX_SIZE * (box_row    )
        end_row      = BOX_SIZE * (box_row + 1)
        start_column = BOX_SIZE * (box_column    )
        end_column   = BOX_SIZE * (box_column + 1)
        return value in self.solution[start_row:end_row,
                                      start_column:end_column]

    #------------------------------
    # Solution generation
    #------------------------------

    def _add_solution(self, row, column, value):
        self.solution[row][column]      = value
        self.solution.mask[row][column] = False

    def _enumerate_solutions(self, row, column, previous_guesses=None):
        if previous_guesses is None:
            values_to_check = np.arange(PUZZLE_SIZE) + 1 
        else:
            values_to_check = previous_guesses
        return np.array([v for v in values_to_check 
                           if self._is_possible_solution(row, column, v)])
        
    #------------------------------
    # Pretty-printing helpers
    #------------------------------

    BORDER_LR     = '|'
    BORDER_TB     = '-'
    BOX_CORNER    = '+'
    BOX_SEPARATOR = ' %s ' % BORDER_LR
    MISSING       = ' '

    def _print_rule(self):
        rule_string = ''.join([self.BOX_CORNER,
                               self.BOX_CORNER.join(['-'*(2*BOX_SIZE+1)]*3),
                               self.BOX_CORNER])
        print rule_string

    def _print_row(self, row):
        
        boxed_rows = row.reshape((BOX_SIZE, BOX_SIZE))
        box_string = self.BOX_SEPARATOR.join([' '.join(['%d' % v for v in box ])
                                              for box in boxed_rows])
        row_string = ' '.join([self.BORDER_LR, box_string, self.BORDER_LR])
        print row_string.replace('0', self.MISSING)

def run_solver(puzzle):
    print ' *** Initial Solution ***'
    puzzle.print_solution()
    puzzle.solve()
    print ' ***  Final Solution  ***'
    puzzle.print_solution()

def test():
    my_puzzle = Puzzle('puzzle2.dat')
    run_solver(my_puzzle)
    
def main():
    try:
        my_puzzle = Puzzle(sys.argv[1])
        run_solver(my_puzzle)
    except:
        test()

if __name__ == "__main__":
    main()
