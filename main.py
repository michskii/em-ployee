class IntegerToRoman:
    def __init__(self):
        self.value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

    def validate_number(self, num):
        """Validate if the number is within the acceptable range."""
        if not (0 < num < 4000):
            raise ValueError("Number must be between 1 and 3999")

    def convert_to_roman(self, num):
        """Convert an integer to a Roman numeral."""
        self.validate_number(num)
        roman_numeral = ""
        for value, symbol in self.value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

# Example usage:
if __name__ == "__main__":
    converter = IntegerToRoman()
    number = 1987
    print(f"The Roman numeral for {number} is {converter.convert_to_roman(number)}")