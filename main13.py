def get_squares_and_separate():
    try:
        start = int(input("Enter the start of the range: "))
        end = int(input("Enter the end of the range: "))
        
        squares = [x**2 for x in range(start, end + 1)]
        even_squares = [num for num in squares if num % 2 == 0]
        odd_squares = [num for num in squares if num % 2 != 0]
        
        print("Squares:", squares)
        print("Even Squares:", even_squares)
        print("Odd Squares:", odd_squares)
    except ValueError:
        print("Please enter valid integers for the range.")

if __name__ == "__main__":
    get_squares_and_separate()