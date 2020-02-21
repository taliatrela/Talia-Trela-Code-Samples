#     This project was called 'Checkered Future'. It finds the maximum number of jumps a king checker can make in one turn. 
# Its input contains multiple test cases. The first line of the input contains the number of test cases for that file. The 
# next line then specifies the number of your pieces and the number of your opponent's pieces (m, n) separated by a space. 
# The next m lines contain two integers indicating the row and column of your pieces, separated by a space. The first piece
# is the king. The n lines after that represent the row and column of your opponent's pieces, again separated by a space. 
# For each test case, the output displays the max number of jumps the king can make. 

class Board:
    RED = 'R'
    WHITE = 'W'
    BLANK = ' '

    def __init__(self):
        self._board = []
        for row in range(8):
            self._board.append([])
            for col in range(8):
                self._board[row].append(' ')

    def __str__(self):
        return ('\n').join(str(row) for row in self._board)

    def print(self):
        print(self.__str__())
        return

    def add_checker(self, who, row, col):
        self._board[row][col] = who

    def reset(self):
        self._board = []
        for row in range(8):
            self._board.append([])
            for col in range(8):
                self._board[row].append(' ')

# The '_is_possible_to_jump' methods check to see if the checker will be within bounds if it jumps, and if there is a
# blank space to jump to. It does NOT check if there is an opponent checker that it can jump over.
    def _is_possible_to_jump_diagonally_upright(self, row, col):
        if self._board[row][col] == Board.BLANK:
            return False
        if ((2 <= row <= 7) and (0 <= col <= 5)) and self._board[row - 2][col + 2] == Board.BLANK:
            return True
        return False

    def _is_possible_to_jump_diagonally_downright(self, row, col):
        if self._board[row][col] == Board.BLANK:
            return False
        if ((0 <= row <= 5) and (0 <= col <= 5)) and self._board[row + 2][col + 2] == Board.BLANK:
            return True
        return False

    def _is_possible_to_jump_diagonally_upleft(self, row, col):
        if self._board[row][col] == Board.BLANK:
            return False
        if ((2 <= row <= 7) and (2 <= col <= 7)) and self._board[row - 2][col - 2] == Board.BLANK:
            return True
        return False

    def _is_possible_to_jump_diagonally_downleft(self, row, col):
        if self._board[row][col] == Board.BLANK:
            return False
        if ((0 <= row <= 5) and (2 <= col <= 7)) and self._board[row + 2][col - 2] == Board.BLANK:
            return True
        return False

# These '_can_jump' methods check to see that the checker actually can jump, given that there is an opponent checker to
# jump over and an empty space to jump to.
    def _can_jump_diagonally_upright(self, row, col):
        if self._board[row][col] == Board.RED:
            if self._is_possible_to_jump_diagonally_upright(row, col) and self._board[row-1][col+1] == Board.WHITE:
                return True

        elif self._board[row][col] == Board.WHITE:
            if self._is_possible_to_jump_diagonally_upright(row, col) and self._board[row-1][col+1] == Board.RED:
                return True

        return False

    def _can_jump_diagonally_downright(self, row, col):
        if self._board[row][col] == Board.RED:
            if self._is_possible_to_jump_diagonally_downright(row, col) and self._board[row+1][col+1] == Board.WHITE:
                return True

        elif self._board[row][col] == Board.WHITE:
            if self._is_possible_to_jump_diagonally_downright(row, col) and self._board[row+1][col+1] == Board.RED:
                return True

        return False

    def _can_jump_diagonally_upleft(self, row, col):
        if self._board[row][col] == Board.RED:
            if self._is_possible_to_jump_diagonally_upleft(row, col) and self._board[row-1][col-1] == Board.WHITE:
                return True

        elif self._board[row][col] == Board.WHITE:
            if self._is_possible_to_jump_diagonally_upleft(row, col) and self._board[row-1][col-1] == Board.RED:
                return True

        return False

    def _can_jump_diagonally_downleft(self, row, col):
        if self._board[row][col] == Board.RED:
            if self._is_possible_to_jump_diagonally_downleft(row, col) and self._board[row+1][col-1] == Board.WHITE:
                return True

        elif self._board[row][col] == Board.WHITE:
            if self._is_possible_to_jump_diagonally_downleft(row, col) and self._board[row+1][col-1] == Board.RED:
                return True

        return False

    def _num_jumps(self, row, col, current_jumps=0, list_of_jumps=None):
        if list_of_jumps == None:
            list_of_jumps = []
        else:
            list_of_jumps = list_of_jumps
        # Got the idea to use a default parameter to count the number of jumps (a changing variable in a recursive
        # function) from:
        # https://stackoverflow.com/questions/47276423/python-recursive-function-call-with-changing-variable-value

        # Figured out how to avoid using a mutable empty list as a parameter by using the keyword 'None' instead from:
        # https://docs.python-guide.org/writing/gotchas/
        current_jumps = current_jumps

        if self._can_jump_diagonally_upright(row, col):
            character = self._board[row][col]
            self._board[row][col] = Board.BLANK
            self._board[row - 1][col+1] = Board.BLANK
            self._board[row-2][col+2] = character
            current_jumps += 1

            self._num_jumps(row - 2, col + 2, current_jumps, list_of_jumps)

            current_jumps -= 1
            self._board[row - 2][col+2] = Board.BLANK
            self._board[row][col] = character
            if character == Board.RED:
                self._board[row-1][col+1] = Board.WHITE
            else:
                self._board[row-1][col+1] = Board.RED

        if self._can_jump_diagonally_downright(row, col):
            character = self._board[row][col]
            self._board[row][col] = Board.BLANK
            self._board[row + 1][col+1] = Board.BLANK
            self._board[row+2][col+2] = character
            current_jumps += 1

            self._num_jumps(row + 2, col + 2, current_jumps, list_of_jumps)

            current_jumps -= 1
            self._board[row+2][col+2] = Board.BLANK
            self._board[row][col] = character
            if character == Board.RED:
                self._board[row+1][col+1] = Board.WHITE
            else:
                self._board[row+1][col+1] = Board.RED

        if self._can_jump_diagonally_upleft(row, col):
            character = self._board[row][col]
            self._board[row][col] = Board.BLANK
            self._board[row - 1][col - 1] = Board.BLANK
            self._board[row - 2][col - 2] = character
            current_jumps += 1

            self._num_jumps(row - 2, col - 2, current_jumps, list_of_jumps)

            current_jumps -= 1
            self._board[row - 2][col - 2] = Board.BLANK
            self._board[row][col] = character
            if character == Board.RED:
                self._board[row - 1][col - 1] = Board.WHITE
            else:
                self._board[row - 1][col - 1] = Board.RED

        if self._can_jump_diagonally_downleft(row, col):
            character = self._board[row][col]
            self._board[row][col] = Board.BLANK
            self._board[row + 1][col - 1] = Board.BLANK
            self._board[row + 2][col - 2] = character
            current_jumps += 1

            self._num_jumps(row + 2, col - 2, current_jumps, list_of_jumps)

            current_jumps -= 1
            self._board[row + 2][col - 2] = Board.BLANK
            self._board[row][col] = character
            if character == Board.RED:
                self._board[row + 1][col - 1] = Board.WHITE
            else:
                self._board[row + 1][col - 1] = Board.RED

        if (not self._can_jump_diagonally_upright(row, col)) and (not self._can_jump_diagonally_downright(row, col)) \
                and (not self._can_jump_diagonally_upleft(row, col)) and \
                (not self._can_jump_diagonally_downleft(row, col)):
            list_of_jumps.append(current_jumps)

        return max(list_of_jumps)

    def num_jumps(self, row, col):
        return self._num_jumps(row, col)


def perform_tests_on_inputs(filename, board):
    with open(filename) as myfile:
        num_test_cases = int(myfile.readline())
        print("\nTest file: {}".format(filename))
        for test_case in range(num_test_cases):
            board.reset()
            num_white_pieces, num_red_pieces = [int(num) for num in myfile.readline().split()]
            if num_white_pieces > 0:
                white_king_row , white_king_col = [int(num) for num in myfile.readline().split()]
                board.add_checker('W', white_king_row, white_king_col)
                for white_piece in range(num_white_pieces - 1):
                    row , col = [int(num) for num in myfile.readline().split()]
                    board.add_checker('W', row, col)
            if num_red_pieces > 0:
                red_king_row , red_king_col = [int(num) for num in myfile.readline().split()]

                # NOTE: I made a king red checker in case of the event that there's no white checkers, like in file
                # input11.txt. This way, it will try to find the max jumps of this red checker, since there's no white
                # checkers to find the max jumps of. The answer should still be 0, since the red checker would not be
                # able to jump over anything.

                # I originally had it so that if the number of white pieces was not > 0, to just output that the number
                # of jumps is 0, but then I wouldn't be calling the max_jumps function. That's why I just chose the
                # first red piece to find the max number of jumps of. I could have also just chosen a random spot
                # to find the max jumps, and since it was empty, it wouldn't be able to jump, but I didn't
                # know which spot to choose. So I just went with the king red checker.

                board.add_checker('R', red_king_row, red_king_col)
                for red_piece in range(num_red_pieces - 1):
                    row, col = [int(num) for num in myfile.readline().split()]
                    board.add_checker('R', row, col)

            if num_white_pieces > 0:
                max_jumps = board.num_jumps(white_king_row, white_king_col)
                print("Test case {} --> the number of jumps is {}".format(test_case + 1, max_jumps))
            elif num_red_pieces > 0:
                max_jumps = board.num_jumps(red_king_row, red_king_col)
                # In the event that there's no white pieces, find the max jumps of the king red checker
                # (should still be 0)
                print("Test case {} --> the number of jumps is {}".format(test_case + 1, max_jumps))


# Tests for max jumps with input files 1 through 17:
if __name__ == '__main__':

    my_board = Board()
    for n in range(1, 18):
        perform_tests_on_inputs("inputs/input{}.txt".format(n), my_board)


#  NOTE: For the file 'input13.txt', I deleted one of the duplicate data points, (3, 7), because there was already
#  a (3, 7) data point listed for the red pieces. The first line said that there was supposed to be 13 red pieces,
#  but 14 were listed, so it caused an error when reading from the file. I deleted it because I knew it
#  would not affect the board and the results.
