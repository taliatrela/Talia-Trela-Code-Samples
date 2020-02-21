#   The purpose of this project was to use linked classes and operator overloading. We were to write implementations for 
# a class of polynomial operations, including addition, multiplication, differentiation, and integration. We also had to
# make unit tests for each of our methods.


class TermNode:
    def __init__(self, exponent, coefficient, next=None):
        self.exponent = exponent
        self.coefficient = coefficient
        self.next = next

    def __eq__(self, other):
        if (self.exponent == other.exponent) and (self.coefficient == other.coefficient):
            return True
        return False

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __str__(self):
        if self.coefficient == 0:
            return '0'
        if self.exponent == 0:
            return '{:.2f}'.format(self.coefficient)
        if self.exponent == 1:
            return '{:.2f}x'.format(self.coefficient)
        return '{:.2f}x^{}'.format(self.coefficient, self.exponent)
# Learned how to get two decimal places using string formatting from:
# https://stackoverflow.com/questions/6149006/display-a-float-with-two-decimal-places-in-python/6149115


class Polynomial:
    def __init__(self, exponent, coefficient):
        if (type(exponent) not in [float, int]) or (type(coefficient) not in [float, int]):
            raise ValueError("Invalid exponent and/or coefficient. Must be a float or an int.")
        self._first_node = TermNode(exponent, coefficient)
        # The exponent can be a float in case it is a fraction / rational number.

    def __str__(self):
        string = ''
        current_node = self._first_node

        while current_node is not None:
            if string == '':
                string += '{}'.format(str(current_node))
            else:
                if current_node.coefficient >= 0:
                    string += ' + {}'.format(str(current_node))
                else:
                    if current_node.exponent == 0:
                        string += ' - {:.2f}'.format(-1*current_node.coefficient)
                    elif current_node.exponent == 1:
                        string += ' - {:.2f}x'.format(-1*current_node.coefficient)
                    else:
                        string += ' - {:.2f}x^{}'.format(-1*current_node.coefficient, current_node.exponent)

            current_node = current_node.next

        return string
# The above string function removes the plus sign in front of negative coefficients.
# So, instead of resulting in a string like '2x^4 + -3x^3 + -2x^2', it would result in '2x^4 - 3x^3 - 2x^2',
# making it 'cleaner'. However, I also wrote the code for the first formatting way, and copied it at the bottom of
# this file for reference.

    def __eq__(self, other):
        self_term = self._first_node
        other_term = other._first_node

        while (self_term is not None) and (other_term is not None):
            if self_term != other_term:
                return False
            self_term = self_term.next
            other_term = other_term.next

        # If we come out of the loop and one of them still has terms left, they can't be equal!
        if self_term is not None or other_term is not None:
            return False

        # This means they ended the loop by both being none, so all of their other terms were equal.
        return True

    def __ne__(self, other):
        if self == other:
            return False
        return True

    def __add__(self, other):
        if type(other) not in [type(self), int]:
            raise TypeError("Cannot add the two objects together. Must be a polynomial or integer.")
        if type(other) == int:  # This allows someone to add an integer, which actually is a polynomial with x^0
            other = Polynomial(0, other)

        terms_of_new_polynomial = {}
        self_term = self._first_node
        other_term = other._first_node

        while self_term is not None:
            terms_of_new_polynomial[self_term.exponent] = self_term.coefficient
            self_term = self_term.next

        while other_term is not None:
            if other_term.exponent not in terms_of_new_polynomial:
                terms_of_new_polynomial[other_term.exponent] = other_term.coefficient
            else:
                terms_of_new_polynomial[other_term.exponent] += other_term.coefficient
            other_term = other_term.next

        # Figured out how to sort a dictionary by its keys, and in reverse, from:
        # https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
        exponent_keys = sorted(terms_of_new_polynomial.keys(), reverse=True)
        has_at_least_one_term = False
        new_polynomial = None

        # The following will only include non-zero terms in the new polynomial.
        for n in range(len(exponent_keys)):
            if (not has_at_least_one_term) and (terms_of_new_polynomial[exponent_keys[n]] != 0):
                new_polynomial = Polynomial(exponent_keys[n], terms_of_new_polynomial[exponent_keys[n]])
                current_new_polynomial_term = new_polynomial._first_node
                has_at_least_one_term = True
            elif has_at_least_one_term and (terms_of_new_polynomial[exponent_keys[n]] != 0):
                term_to_add = TermNode(exponent_keys[n], terms_of_new_polynomial[exponent_keys[n]])
                current_new_polynomial_term.next = term_to_add
                current_new_polynomial_term = current_new_polynomial_term.next

        # If all of the terms cancel, no terms were added, so new_polynomial should be 'None'.
        # Now the new polynomial that is returned only has ONE zero term, with just coefficient 0
        # (could be any coefficient, but I just chose 0 to make it simple)
        if new_polynomial is None:
            return Polynomial(0, 0)

        return new_polynomial

    def __mul__(self, other):
        if type(other) not in [type(self), int]:
            raise TypeError("Cannot multiply the two objects together. Must be a polynomial or integer.")
        if type(other) == int:
            other = Polynomial(0, other)

        self_term = self._first_node
        new_polynomial = None
        while self_term is not None:
            other_term = other._first_node
            while other_term is not None:
                if new_polynomial is None:
                    new_polynomial = Polynomial(self_term.exponent + other_term.exponent,
                                                self_term.coefficient * other_term.coefficient)
                else:
                    new_polynomial += Polynomial(self_term.exponent + other_term.exponent,
                                                 self_term.coefficient * other_term.coefficient)
                other_term = other_term.next
            self_term = self_term.next
        return new_polynomial

    def differentiate(self):
        self_term = self._first_node
        differentiated_polynomial = None

        # If exponent is 0, the term is a constant, so its derivative is 0. Thus, it doesn't need to be included
        # in the final differentiated polynomial (because adding 0 will not change the final differentiated polynomial)
        while self_term is not None:
            if (differentiated_polynomial is None) and self_term.exponent != 0:
                differentiated_polynomial = Polynomial(self_term.exponent - 1,
                                                       self_term.coefficient * self_term.exponent)
            elif (differentiated_polynomial is not None) and self_term.exponent != 0:
                differentiated_polynomial += Polynomial(self_term.exponent - 1,
                                                        self_term.coefficient * self_term.exponent)
            self_term = self_term.next

        if differentiated_polynomial is None:
            return Polynomial(0, 0)
            # Returns the standard 0 polynomial (with exponent 0) if the original polynomial was a constant

        return differentiated_polynomial

    def integrate(self):
        self_term = self._first_node
        integrated_polynomial = None
        while self_term is not None:
            if integrated_polynomial is None and self_term.exponent != -1:
                integrated_polynomial = Polynomial(self_term.exponent + 1,
                                                   self_term.coefficient / (self_term.exponent + 1))
            elif (integrated_polynomial is not None) and self_term.exponent != -1:
                integrated_polynomial += Polynomial(self_term.exponent + 1,
                                                    self_term.coefficient / (self_term.exponent + 1))
            elif self_term.exponent == -1:
                raise ZeroDivisionError("Cannot integrate with exponent of -1.")
            self_term = self_term.next
        return integrated_polynomial


if __name__ == '__main__':

    # Example use of functions given from the instructions:
    poly2 = Polynomial(3, 2)
    print(poly2)
    poly3 = Polynomial(4, 3)
    print(poly3)
    poly1 = poly2 + poly3
    print(poly1)
    poly3 = poly2 * poly1
    print(poly3)
    poly4 = poly3.differentiate()
    print(poly4)
    poly5 = poly1.integrate()
    print(poly5)

    # My own example:
    print()
    one = Polynomial(20, 3)
    two = Polynomial(9, 4)
    three = Polynomial(-10, 6)
    first = three + two + one
    print(first)
    four = Polynomial(6, 23)
    five = Polynomial(4, 31)
    six = Polynomial(0, -1/3)
    second = six + five + four
    print(second)
    third = second + first
    print(third)
    fourth = third.differentiate()
    print(fourth)
    fifth = third.integrate()
    print(fifth)
    print(first * second)

'''
# This is the other string method that wouldn't remove the 'plus' signs for negative coefficients. 
    def __str__(self):
        string = ''
        current_node = self._first_node

        while current_node is not None:
            if string == '':
                string += '{}'.format(str(current_node))
            else:
                string += ' + {}'.format(str(current_node))
            current_node = current_node.next

        return string

'''
