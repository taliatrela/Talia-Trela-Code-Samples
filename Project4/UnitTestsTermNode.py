from unittest import TestCase
from Project4 import TermNode


class TestTermNode(TestCase):
    def test__init__(self):
        # Arrange
        exponent = 2
        coefficient = 4

        # Act
        first_term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(first_term.coefficient, coefficient)
        self.assertEqual(first_term.exponent, exponent)
        self.assertEqual(first_term.next, None)

    def test__eq___when_terms_are_equal(self):
        # Arrange
        exponent = 2
        coefficient = 4

        # Act
        first_term = TermNode(exponent, coefficient)
        second_term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(first_term, second_term)

    def test__eq___when_terms_are_not_equal(self):
        # First case: exponents not equal
        # Arrange / Act
        first_term = TermNode(4, 2)
        second_term = TermNode(3, 2)

        # Assert
        self.assertFalse(first_term == second_term)

        # Second case: coefficients not equal
        # Arrange / Act
        first_term = TermNode(4, 3)
        second_term = TermNode(4, 2)

        # Assert
        self.assertFalse(first_term == second_term)

        # Third case: both exponent and coefficient not equal
        # Arrange / Act
        first_term = TermNode(4, 5)
        second_term = TermNode(3, 2)

        # Assert
        self.assertFalse(first_term == second_term)

    def test___ne___when_terms_not_equal(self):
        # First case: exponents not equal
        # Arrange / Act
        first_term = TermNode(4, 2)
        second_term = TermNode(3, 2)

        # Assert
        self.assertNotEqual(first_term, second_term)

        # Second case: coefficients not equal
        # Arrange / Act
        first_term = TermNode(4, 3)
        second_term = TermNode(4, 2)

        # Assert
        self.assertNotEqual(first_term, second_term)

        # Third case: both exponent and coefficient not equal
        # Arrange / Act
        first_term = TermNode(4, 5)
        second_term = TermNode(3, 2)

        # Assert
        self.assertNotEqual(first_term, second_term)

    def test___ne___when_terms_are_equal(self):
        # Arrange
        exponent = 2
        coefficient = 4

        # Act
        first_term = TermNode(exponent, coefficient)
        second_term = TermNode(exponent, coefficient)

        # Assert
        self.assertFalse(first_term != second_term)

    def test__str__coeffcient_0(self):
        # Arrange
        exponent = 2
        coefficient = 0
        expected_string = '0'

        # Act
        term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(str(term), expected_string)

    def test__str__exponent_0(self):
        # Arrange
        exponent = 0
        coefficient = 1.4956
        expected_string = '1.50'

        # Act
        term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(str(term), expected_string)

    def test__str__exponent_1(self):
        # Arrange
        exponent = 1
        coefficient = 1.4956
        expected_string = '1.50x'

        # Act
        term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(str(term), expected_string)

    def test__str__exponent_coefficient_both_not_0(self):
        # First case: coefficient positive
        # Arrange
        exponent = 3
        coefficient = 1.4956
        expected_string = '1.50x^3'

        # Act
        term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(str(term), expected_string)

        # Second case: coefficient negative
        # Arrange
        exponent = 3
        coefficient = -1.4956
        expected_string = '-1.50x^3'

        # Act
        term = TermNode(exponent, coefficient)

        # Assert
        self.assertEqual(str(term), expected_string)




