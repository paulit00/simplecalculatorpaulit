class Calculator:

    def __init__(self, number=0):
        if isinstance(number, (int, float)):
            self.starting_number = float(number)
            self.result = float(number)
        else:
            raise ValueError('Value has to be a real number')

    def reset(self):
        self.result = self.starting_number
        return self.result

    def add(self, number_to_add):
        if isinstance(number_to_add, (int, float)):
            self.result += number_to_add
            return self.result
        else:
            raise ValueError('Value has to be a real number')

    def subtract(self, number_to_subtract):
        if isinstance(number_to_subtract, (int, float)):
            self.result -= number_to_subtract
            return self.result
        else:
            raise ValueError('Value has to be a real number')

    def multiply(self, number_to_multiply):
        if isinstance(number_to_multiply, (int, float)):
            self.result *= number_to_multiply
            return self.result
        else:
            raise ValueError('Value has to be a real number')

    def divide(self, number_to_divide_by):
        if isinstance(number_to_divide_by, (int, float)):
            if number_to_divide_by == 0:
                raise ZeroDivisionError('Error. Can not divide by 0.')
            self.result /= number_to_divide_by
            return self.result
        else:
            raise ValueError('Value has to be a real number')

    def root(self, n_root_of_a_number):
        if isinstance(n_root_of_a_number, (int, float)):
            if self.result < 0 and n_root_of_a_number % 2 == 0:
                raise ValueError('Can not take even root out of negative numbers.')
            elif n_root_of_a_number == 0:
                raise ZeroDivisionError('Error. Can not divide by 0.')
            else:
                self.result = self.result ** (1 / n_root_of_a_number)
                return self.result
        else:
            raise ValueError('Value has to be a real number')
