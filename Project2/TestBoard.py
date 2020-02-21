from unittest import TestCase
from Project2Recursion import Board


class TestBoard(TestCase):
    def test___init__(self):
        # Arrange
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                          ]
        # Act
        my_board = Board()

        # Assert
        self.assertEqual(my_board._board, expected_board)

    def test___str__(self):
        # Arrange
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                          ]
        string_of_board = ('\n').join(str(row) for row in expected_board)

        # Act
        my_board = Board()

        # Assert
        self.assertEqual(my_board.__str__(), string_of_board)

    def test_add_checker(self):
        # Arrange
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', 'B', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                          ]

        # Act
        my_board = Board()
        my_board.add_checker('B', 2, 1)

        # Assert
        self.assertEqual(my_board._board, expected_board)

    def test_reset(self):
        # Arrange
        expected_board = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                          [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
                          ]

        # Act
        my_board = Board()
        my_board.add_checker('B', 2, 1)
        my_board.add_checker('R', 7, 7)
        my_board.reset()

        # Assert
        self.assertEqual(my_board._board, expected_board)

    def test_is_possible_to_jump_diagonally_upright(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 0, 7)
        my_board.add_checker('W', 3, 1)
        my_board.add_checker('R', 2, 2)

        # Assert that the checker cannot possibly jump diagonally upright given its position.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upright(0, 7), False)

        # Assert that if the space is empty, it cannot jump upright because there is no checker there.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upright(7, 1), False)

        # Assert that it is possible to jump upright if there is a checker to be moved and an empty space to jump to.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upright(3, 1), True)

    def test_is_possible_to_jump_diagonally_downright(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 0, 7)
        my_board.add_checker('W', 3, 1)
        my_board.add_checker('R', 4, 2)

        # Assert that the checker cannot possibly jump diagonally downright given its position.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_downright(0, 7), False)

        # Assert that if the space is empty, it cannot jump downright because there is no checker there.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_downright(3, 3), False)

        # Assert that it is possible to jump downright if there is a checker to be moved and an empty space to jump to.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_downright(3, 1), True)

    def test__is_possible_to_jump_diagonally_upleft(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 0, 7)
        my_board.add_checker('W', 5, 4)
        my_board.add_checker('R', 4, 3)

        # Assert that the checker cannot possibly jump diagonally up-left given its position.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upleft(0, 7), False)

        # Assert that if the space is empty, it cannot jump up-left because there is no checker there.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upleft(4, 4), False)

        # Assert that it is possible to jump up-left if there is a checker to be moved and an empty space to jump to.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upleft(5, 4), True)

    def test_is_possible_to_jump_diagonally_downleft(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 6, 6)
        my_board.add_checker('W', 3, 2)
        my_board.add_checker('R', 2, 3)

        # Assert that the checker cannot possibly jump diagonally down-left given its position.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_downleft(6, 6), False)

        # Assert that if the space is empty, it cannot jump down-left because there is no checker there.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_downleft(4, 4), False)

        # Assert that it is possible to jump up-left if there is a checker to be moved and an empty space to jump to.
        self.assertEqual(my_board._is_possible_to_jump_diagonally_upleft(3, 2), True)

    def test_can_jump_diagonally_upright(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('R', 5, 5)
        my_board.add_checker('W', 4, 6)
        my_board.add_checker('W', 7, 1)
        my_board.add_checker('R', 6, 2)
        my_board.add_checker('W', 4, 1)

        # Assert that the red checker can jump over the white checker if possible.
        self.assertEqual(my_board._can_jump_diagonally_upright(5, 5), True)

        # Assert that the white checker can jump over the red checker, if possible.
        self.assertEqual(my_board._can_jump_diagonally_upright(7, 1), True)

        # Assert that a red checker can't jump if there's no white checker to jump over.
        self.assertEqual(my_board._can_jump_diagonally_upright(6, 2), False)

        # Assert that a white checker can't jump if there's no red checker to jump over.
        self.assertEqual(my_board._can_jump_diagonally_upright(4, 1), False)

    def test__can_jump_diagonally_downright(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('R', 5, 5)
        my_board.add_checker('W', 6, 6)
        my_board.add_checker('W', 5, 1)
        my_board.add_checker('R', 6, 2)
        my_board.add_checker('R', 4, 5)
        my_board.add_checker('W', 4, 1)

        # Assert that the red checker can jump over the white checker if possible.
        self.assertEqual(my_board._can_jump_diagonally_downright(5, 5), True)

        # Assert that the white checker can jump over the red checker, if possible.
        self.assertEqual(my_board._can_jump_diagonally_downright(5, 1), True)

        # Assert that a red checker can't jump if there's no white checker to jump over.
        self.assertEqual(my_board._can_jump_diagonally_downright(4, 5), False)

        # Assert that a white checker can't jump if there's no red checker to jump over.
        self.assertEqual(my_board._can_jump_diagonally_downright(4, 1), False)

    def test_can_jump_diagonally_upleft(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 1, 1)
        my_board.add_checker('W', 1, 3)
        my_board.add_checker('R', 1, 5)
        my_board.add_checker('R', 2, 2)
        my_board.add_checker('W', 2, 4)
        my_board.add_checker('R', 2, 6)
        my_board.add_checker('W', 3, 3)
        my_board.add_checker('R', 5, 2)
        my_board.add_checker('W', 6, 3)

        # Assert that a red checker can jump over a white, if possible.
        self.assertEqual(my_board._can_jump_diagonally_upleft(2, 2), True)

        # Assert that a white checker can jump over a red, if possible.
        self.assertEqual(my_board._can_jump_diagonally_upleft(6, 3), True)

        # Assert that a white checker cannot jump over a red checker if the space after the red checker is occupied.
        self.assertEqual(my_board._can_jump_diagonally_upleft(3, 3), False)

        # Assert that a white checker cannot jump over a white checker.
        self.assertEqual(my_board._can_jump_diagonally_upleft(2, 4), False)

        # Assert that a red checker cannot jump over a red checker.
        self.assertEqual(my_board._can_jump_diagonally_upleft(2, 6), False)

    def test__can_jump_diagonally_downleft(self):
        # Arrange
        my_board = Board()

        # Act
        my_board.add_checker('W', 1, 1)
        my_board.add_checker('W', 1, 3)
        my_board.add_checker('R', 1, 5)
        my_board.add_checker('R', 2, 2)
        my_board.add_checker('W', 2, 4)
        my_board.add_checker('R', 2, 6)
        my_board.add_checker('R', 5, 2)
        my_board.add_checker('W', 6, 3)
        my_board.add_checker('R', 4, 3)
        my_board.add_checker('W', 5, 4)
        my_board.add_checker('W', 3, 5)
        my_board.add_checker('R', 2, 6)
        my_board.add_checker('W', 1, 7)

        # Assert that a red checker can jump over a white, if possible.
        self.assertEqual(my_board._can_jump_diagonally_downleft(1, 5), True)

        # Assert that a white checker can jump over a red, if possible.
        self.assertEqual(my_board._can_jump_diagonally_downleft(1, 3), True)

        # Assert that a white checker cannot jump over a red checker if the space after the red checker is occupied.
        self.assertEqual(my_board._can_jump_diagonally_downleft(1, 7), False)

        # Assert that a white checker cannot jump over a white checker.
        self.assertEqual(my_board._can_jump_diagonally_downleft(5, 4), False)

        # Assert that a red checker cannot jump over a red checker.
        self.assertEqual(my_board._can_jump_diagonally_downleft(4, 3), False)
