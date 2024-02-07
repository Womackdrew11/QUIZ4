from folder1.square import calculate_square
from folder2.even import is_even
from folder3.case import convert_to_uppercase

def main():
    number = 5
    square_result = calculate_square(number)

    is_even_result = is_even(number)

    input_string = "hello"
    uppercase_result = convert_to_uppercase(input_string)

    print(f"Square of {number}: {square_result}\n")

    print(f"Is {number} even? {is_even_result}\n")

    print(f"Uppercase of '{input_string}': {uppercase_result}")

if __name__ == "__main__":
    main()
