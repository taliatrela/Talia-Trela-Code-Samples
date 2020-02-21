from unittest import TestCase
from Project4 import Polynomial, TermNode


class TestPolynomial(TestCase):
    def test___init__(self):
        # Arrange
        exponent = 3
        coefficient = 2

        my_poly = Polynomial(exponent, coefficient)

        self.assertTrue(my_poly._first_node)  # Make sure first node was created
        self.assertEqual(type(my_poly._first_node), TermNode)  # Make sure first node is an instance of term node
        self.assertEqual(my_poly._first_node.exponent, exponent)  # Make sure term node was created with same exponent
        self.assertEqual(my_poly._first_node.coefficient, coefficient)  # and same coefficient that was given.

    def test___init__when_invalid_exponent_is_given(self):
        # Arrange
        exponent = 'a'  # Should raise an exception.
        coefficient = 2

        # Act / Assert
        with self.assertRaises(ValueError):
            Polynomial(exponent, coefficient)

    def test___init__when_invalid_coefficient_is_given(self):
        # Arrange
        exponent = 1/3
        coefficient = None  # Should raise an exception if no coefficient is given.

        # Act / Assert
        with self.assertRaises(ValueError):
            Polynomial(exponent, coefficient)

    def test__str__multiple_terms(self):
        # First case: all positive terms
        # Arrange:
        poly1 = Polynomial(0, 5)  # constant
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3
        expected_string = '4.00x^10 + 4.00x^3 + 5.00'

        # Act / Assert
        self.assertEqual(str(poly4), expected_string)

        # Second case: all negative terms
        # Arrange:
        poly1 = Polynomial(0, -5)  # constant (exponent = 0)
        poly2 = Polynomial(1, -4)  # exponent = 1
        poly3 = Polynomial(10, -4)  # positive exponent
        poly4 = Polynomial(20, -3)  # first term negative
        poly4 = poly1 + poly2 + poly3 + poly4
        expected_string = '-3.00x^20 - 4.00x^10 - 4.00x - 5.00'

        # Act / Assert
        self.assertEqual(str(poly4), expected_string)

    def test__str__with_terms_that_all_have_coefficient_zero(self):
        # Arrange:
        poly1 = Polynomial(0, 0)
        poly2 = Polynomial(3, 0)
        poly3 = Polynomial(10, 0)
        poly4 = poly1 + poly2 + poly3
        expected_string = '0'

        # Act / Assert
        self.assertEqual(str(poly4), expected_string)

    def test__str__with_one_term(self):
        # First case: zero-term, exponent 0
        # Arrange:
        poly1 = Polynomial(0, 0)
        expected_string = '0'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

        # Second case: fractional term, exponent 1
        # Arrange:
        poly1 = Polynomial(1, 1/3)
        expected_string = '0.33x'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

        # Third case: term with negative exponent
        # Arrange:
        poly1 = Polynomial(-3, 4)
        expected_string = '4.00x^-3'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

    def test__str__with_one_term_negative_coefficient(self):
        # First case: exponent 0
        # Arrange:
        poly1 = Polynomial(0, -4)
        expected_string = '-4.00'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

        # Second case: exponent 1
        # Arrange:
        poly1 = Polynomial(1, -1/3)
        expected_string = '-0.33x'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

        # Third case: negative exponent
        # Arrange:
        poly1 = Polynomial(-3, -4)
        expected_string = '-4.00x^-3'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

        # Fourth case: positive exponent
        # Arrange:
        poly1 = Polynomial(3, -4)
        expected_string = '-4.00x^3'

        # Act / Assert
        self.assertEqual(str(poly1), expected_string)

    def test___eq___when_terms_are_all_equal(self):
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 5)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly8 = poly5 + poly6 + poly7

        # Act / Assert
        self.assertEqual(poly4, poly8)

    def test___eq___when_all_but_last_term_equal(self):
        # Arrange:
        poly1 = Polynomial(-2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 5)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly8 = poly5 + poly6 + poly7

        # Act / Assert
        self.assertFalse(poly4 == poly8)

    def test___eq___when_all_terms_equal_but_one_polynomial_has_extra_term(self):
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 5)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly8 = Polynomial(-3, 6)
        poly9 = poly5 + poly6 + poly7 + poly8

        # Act / Assert
        self.assertFalse(poly4 == poly9)

    def test___eq___one_term(self):
        # Case 1: They're equal.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(0, 5)

        # Act / Assert
        self.assertEqual(poly1, poly2)

        # Case 2: They're not equal.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(0, -6)

        # Act / Assert
        self.assertFalse(poly1 == poly2)

    def test___ne___one_term(self):
        # Case 1: They're equal.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(0, 5)

        # Act / Assert
        self.assertFalse(poly1 != poly2)

        # Case 2: They're not equal.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(0, -6)

        # Act / Assert
        self.assertNotEqual(poly1, poly2)

    def test__ne__when_all_terms_equal_but_one_polynomial_has_extra_term(self):
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 5)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly8 = Polynomial(-3, 6)
        poly9 = poly5 + poly6 + poly7 + poly8

        # Act / Assert
        self.assertNotEqual(poly4, poly9)

    def test__ne__when_all_but_last_term_equal(self):
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 6)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly9 = poly5 + poly6 + poly7

        # Act / Assert
        self.assertNotEqual(poly4, poly9)

    def test___ne___when_terms_are_all_equal(self):
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(0, 5)
        poly6 = Polynomial(10, 4)
        poly7 = Polynomial(3, 4)
        poly8 = poly5 + poly6 + poly7

        # Act / Assert
        self.assertFalse(poly4 != poly8)

    def test__add__two_terms_different_exponents(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        expected_string = '4.00x^3 + 5.00x^2'

        # Act
        poly3 = poly1 + poly2

        # Assert
        self.assertEqual(str(poly3), expected_string)
        self.assertEqual(str(poly1), '5.00x^2')  # Make sure the original polynomials didn't change
        self.assertEqual(str(poly2), '4.00x^3')

    def test__add__two_terms_same_exponent(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(2, 4)
        expected_string = '9.00x^2'

        # Act
        poly3 = poly1 + poly2

        # Assert
        self.assertEqual(str(poly3), expected_string)

    def test__add__one_term_to_two_terms(self):
        # First case: no zero terms
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = poly1 + poly2
        poly4 = Polynomial(10, 4)
        expected_string = '4.00x^10 + 4.00x^3 + 5.00x^2'

        # Act
        poly5 = poly3 + poly4

        # Assert
        self.assertEqual(str(poly5), expected_string)

        # Second case: add zero first
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = poly1 + poly2
        poly4 = Polynomial(0, 0)
        expected_string = '4.00x^3 + 5.00x^2'

        # Act
        poly5 = poly4 + poly3

        # Assert
        self.assertEqual(str(poly5), expected_string)

        # Third case: add zero last
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = poly1 + poly2
        poly4 = Polynomial(0, 0)
        expected_string = '4.00x^3 + 5.00x^2'

        # Act
        poly5 = poly3 + poly4

        # Assert
        self.assertEqual(str(poly5), expected_string)

    def test__add__two_polynomials_all_terms_cancel(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(2, -5)
        poly6 = Polynomial(3, -4)
        poly7 = Polynomial(10, -4)
        poly8 = poly5 + poly6 + poly7

        expected_string = '0'

        # Act
        poly9 = poly4 + poly8

        # Assert
        self.assertEqual(str(poly9), expected_string)

    def test__add__two_polynomials_with_negative_exponents(self):
        # Arrange:
        poly1 = Polynomial(-2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(-10, 4)
        poly4 = poly1 + poly2 + poly3

        expected_string1 = '4.00x^3 + 5.00x^-2 + 4.00x^-10'

        self.assertEqual(str(poly4), expected_string1)

        poly5 = Polynomial(-2, -5)
        poly6 = Polynomial(3, -4)
        poly7 = Polynomial(-10, -4)
        poly8 = poly5 + poly6 + poly7

        expected_string = '0'

        # Act
        poly9 = poly4 + poly8

        # Assert
        self.assertEqual(str(poly9), expected_string)

    def test__add__two_polynomials_invalid_types(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        letter = 'a'

        # Act/ Assert
        with self.assertRaises(TypeError):
            poly2 = poly1 + letter

    def test__add__polynomial_and_integer(self):
        # Case 1: Integer is non-zero.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        integer_to_add = 6

        # Act
        poly5 = poly4 + integer_to_add

        expected_string = '4.00x^10 + 4.00x^3 + 11.00'

        # Assert
        self.assertEqual(str(poly5), expected_string)

        # Case 2: Integer is 0.
        # Arrange:
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        integer_to_add = 0
        # Or can use a polynomial...
        zero = Polynomial(0, 0)

        # Act
        poly5 = poly4 + integer_to_add  # Test add 0 when '0' is given.
        poly6 = poly4 + zero            # Test add 0 when 0 is an instance of Polynomial.

        expected_string = '4.00x^10 + 4.00x^3 + 5.00'

        # Assert
        self.assertEqual(str(poly5), expected_string)  # First case, when 0 is given
        self.assertEqual(str(poly6), expected_string)  # Second case, when 0 is an instance of Polynomial

        # Case 3: Integers cancel out.
        # Arrange
        poly1 = Polynomial(0, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        integer_to_add = -5

        # Act
        poly5 = poly4 + integer_to_add

        expected_string = '4.00x^10 + 4.00x^3'

        # Assert
        self.assertEqual(str(poly5), expected_string)

    def test__add__zero_polynomial_and_zero(self):
        # Case 1: Integer is non-zero.
        # Arrange:
        poly1 = Polynomial(5, 0)

        integer_to_add = 0

        # Act
        poly2 = poly1 + integer_to_add
        # Could also add 0 polynomial...
        other_poly2 = poly1 + Polynomial(0, 0)

        expected_string = '0'

        # Assert
        self.assertEqual(str(poly2), expected_string)   # Added 0 integer
        self.assertEqual(str(other_poly2), expected_string)  # Added 0 polynomial

    def test__mul__polynomial_and_constant(self):
        # Arrange
        poly1 = Polynomial(4, 6)
        constant = 7
        # Or, constant can be a polynomial with exponent 0:
        constant2 = Polynomial(0, 7)

        # Act
        poly2 = poly1 * constant
        other_poly2 = poly1 * constant2
        expected_string = '42.00x^4'

        # Assert
        self.assertEqual(str(poly2), expected_string)  # Assert equal when multiplied by constant 7
        self.assertEqual(str(other_poly2), expected_string)  # Assert equal when multiplied by polynomial 7
        self.assertEqual(str(poly1), '6.00x^4')  # Make sure original polynomial didn't change

    def test__mul__polynomial_and_zero(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        # Act
        poly5 = poly4 * 0
        # Again, 0 can also be a polynomial with exponent 0...
        other_poly5 = poly4 * Polynomial(0, 0)
        expected_string = '0'

        # Assert
        self.assertEqual(str(poly5), expected_string)  # Assert it's 0 when multiplied directly by 0
        self.assertEqual(str(other_poly5), expected_string)  # Assert it's 0 when multiplied by polynomial 0
        self.assertEqual(str(poly4), '4.00x^10 + 4.00x^3 + 5.00x^2') # Assert original polynomial didn't change

    def test__mul__polynomial_with_three_terms_and_polynomial_with_one_term(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        poly2 = Polynomial(3, 4)
        poly3 = Polynomial(10, 4)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(-2, -5)

        # Act
        poly6 = poly4 * poly5
        expected_string = '-20.00x^8 - 20.00x - 25.00'

        # Assert
        self.assertEqual(str(poly6), expected_string)

    def test__mul__polynomial_with_negative_exponents(self):
        # Arrange:
        poly1 = Polynomial(-1, 5)
        poly2 = Polynomial(-2, 4)
        poly3 = poly1 + poly2
        poly4 = Polynomial(1, 3)
        poly5 = Polynomial(2, -10)
        poly6 = poly4 + poly5

        # Act
        poly7 = poly3 * poly6
        expected_string = '-50.00x - 25.00 + 12.00x^-1'

        # Assert
        self.assertEqual(str(poly7), expected_string)

    def test__mul__both_polynomials_three_terms_larger_numbers_case(self):
        # Arrange
        poly1 = Polynomial(32, 23)
        poly2 = Polynomial(6, -4)
        poly3 = Polynomial(3, 77)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(5, 4)
        poly6 = Polynomial(8, -6)
        poly7 = Polynomial(10, 9)
        poly8 = poly5 + poly6 + poly7

        # Act
        poly9 = poly4 * poly8
        expected_string = '207.00x^42 - 138.00x^40 + 92.00x^37 - 36.00x^16 + 24.00x^14 + ' \
                          '693.00x^13 - 478.00x^11 + 308.00x^8'
        # Checked the above on paper.

        self.assertEqual(str(poly9), expected_string)

    def test__mul__polynomials_with_unequal_number_of_terms(self):
        # Got the following test case from:
        # https://www.varsitytutors.com/algebra_1-help/how-to-multiply-polynomials
        # Arrange
        poly1 = Polynomial(2, 3)
        poly2 = Polynomial(1, -2)
        poly3 = Polynomial(0, 5)
        poly4 = poly1 + poly2 + poly3

        poly5 = Polynomial(3, -1)
        poly6 = Polynomial(2, 2)
        poly7 = Polynomial(1, -5)
        poly8 = Polynomial(0, -10)
        poly9 = poly5 + poly6 + poly7 + poly8

        # Act
        poly10 = poly4 * poly9
        expected_string = '-3.00x^5 + 8.00x^4 - 24.00x^3 - 10.00x^2 - 5.00x - 50.00'

        # Assert
        self.assertEqual(str(poly10), expected_string)

    def test__mul__two_polynomials_invalid_types(self):
        # Arrange:
        poly1 = Polynomial(2, 5)
        letter = 'a'

        # Act/ Assert
        with self.assertRaises(TypeError):
            poly2 = poly1 * letter

    def test_differentiate_four_terms(self):
        # Arrange
        poly1 = Polynomial(2, 3)
        poly2 = Polynomial(1, -2)
        poly3 = Polynomial(0, 5)
        poly4 = Polynomial(3, -1)
        poly5 = poly1 + poly2 + poly3 + poly4

        # Act
        poly6 = poly5.differentiate()
        expected_string = '-3.00x^2 + 6.00x - 2.00'

        # Assert
        self.assertEqual(str(poly6), expected_string)
        self.assertEqual(str(poly5), '-1.00x^3 + 3.00x^2 - 2.00x + 5.00')  # Assert original polynomial didn't change

    def test_differentiate_rational_exponent(self):
        # Arrange
        poly1 = Polynomial(1/3, 3)

        # Act
        poly2 = poly1.differentiate()
        expected_string = '1.00x^{}'.format(str((1/3)-1))

        # Assert
        self.assertEqual(str(poly2), expected_string)

    def test_differentiate_one_term(self):
        # Case 1: Positive exponent (not equal to 1).
        # Arrange
        poly1 = Polynomial(2, 3)

        # Act
        poly2 = poly1.differentiate()
        expected_string = '6.00x'

        # Assert
        self.assertEqual(str(poly2), expected_string)

        # Case 2: Exponent 1 (so that a constant results)
        # Arrange
        poly1 = Polynomial(1, 3)

        # Act
        poly2 = poly1.differentiate()
        expected_string = '3.00'

        # Assert
        self.assertEqual(str(poly2), expected_string)

        # Case 3: Exponent 0 (thus a constant-- so 0 should result)
        # Arrange
        poly1 = Polynomial(0, 3)

        # Act
        poly2 = poly1.differentiate()
        expected_string = '0'

        # Assert
        self.assertEqual(str(poly2), expected_string)

        # Case 4: Negative exponent
        # Arrange
        poly1 = Polynomial(-3, -5)

        # Act
        poly2 = poly1.differentiate()
        expected_string = '15.00x^-4'

        # Assert
        self.assertEqual(str(poly2), expected_string)

    def test_differentiate_four_terms_all_zero(self):
        # Arrange
        poly1 = Polynomial(2, 0)
        poly2 = Polynomial(1, 0)
        poly3 = Polynomial(0, 0)
        poly4 = Polynomial(3, 0)
        poly5 = poly1 + poly2 + poly3 + poly4

        # Act
        poly6 = poly5.differentiate()
        expected_string = '0'

        # Assert
        self.assertEqual(str(poly6), expected_string)

    def test_integrate_one_term_rational_number(self):
        # Case 1: Rational exponent (not equal to 1).
        # Arrange
        poly1 = Polynomial(1/3, 3)

        # Act
        poly2 = poly1.integrate()
        expected_string = '2.25x^{}'.format(str(4/3))

        # Assert
        self.assertEqual(str(poly2), expected_string)

    def test_integrate_one_term(self):
        # Case 1: Positive exponent (not equal to 1).
        # Arrange
        poly1 = Polynomial(2, 3)

        # Act
        poly2 = poly1.integrate()
        expected_string = '1.00x^3'

        # Assert
        self.assertEqual(str(poly2), expected_string)

        # Case 2: Exponent 0 (a constant)
        # Arrange
        poly1 = Polynomial(0, 3)

        # Act
        poly2 = poly1.integrate()
        expected_string = '3.00x'

        # Assert
        self.assertEqual(str(poly2), expected_string)

        # Case 4: Negative exponent
        # Arrange
        poly1 = Polynomial(-3, -4)

        # Act
        poly2 = poly1.integrate()
        expected_string = '2.00x^-2'

        # Assert
        self.assertEqual(str(poly2), expected_string)

    def test_integrate_multiple_terms(self):
        # Arrange
        poly1 = Polynomial(2, 1)
        poly2 = Polynomial(3, 6)
        poly3 = Polynomial(4, 7)
        poly4 = Polynomial(10, 8)
        poly5 = poly1 + poly2 + poly3 + poly4

        # Act
        poly6 = poly5.integrate()
        expected_string = '0.73x^11 + 1.40x^5 + 1.50x^4 + 0.33x^3'

        # Assert
        self.assertEqual(str(poly6), expected_string)
        self.assertEqual(str(poly5), '8.00x^10 + 7.00x^4 + 6.00x^3 + 1.00x^2') # Assert that original poly didn't change

    def test_integrate_zero_terms(self):
        # Arrange
        poly1 = Polynomial(2, 0)
        poly2 = Polynomial(3, 0)
        poly3 = Polynomial(4, 0)
        poly4 = Polynomial(10, 0)
        poly5 = poly1 + poly2 + poly3 + poly4

        # Act
        poly6 = poly5.integrate()
        expected_string = '0'    # When integrating zero term, get constant. But, constant in this case is just 0.

        # Assert
        self.assertEqual(str(poly6), expected_string)

    def test_integrate_negative_1_exponent(self):
        # Arrange
        poly1 = Polynomial(-1, 3)

        # Act / Assert
        with self.assertRaises(ZeroDivisionError):
            poly2 = poly1.integrate()

