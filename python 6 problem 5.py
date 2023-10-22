def remove_odd_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers
if __name__ == "__main__":

    integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    modified_list = remove_odd_numbers(integer_list)

    print("Original List:", integer_list)
    print("Modified List (even numbers only):", modified_list)
