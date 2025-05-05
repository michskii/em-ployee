class StringReverser:
    @staticmethod
    def reverse_words(input_string):
        """
        Reverses the words in a given string.

        :param input_string: The string to reverse.
        :return: A string with words reversed.
        """
        words = input_string.split()
        reversed_words = words[::-1]
        return ' '.join(reversed_words)


# Example usage
if __name__ == "__main__":
    input_str = "Hello world from Python"
    reverser = StringReverser()
    print(reverser.reverse_words(input_str))