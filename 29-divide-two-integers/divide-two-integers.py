class Solution(object):
    def divide(self, dividend, divisor):

        # Special case
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # Determine the sign
        negative = (dividend < 0) != (divisor < 0)

        # Work with positive numbers
        dividend = abs(dividend)
        divisor = abs(divisor)

        quotient = 0

        # Repeatedly subtract using powers of 2
        while dividend >= divisor:
            temp = divisor
            multiple = 1

            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            quotient += multiple

        # Apply sign
        if negative:
            quotient = -quotient

        return quotient