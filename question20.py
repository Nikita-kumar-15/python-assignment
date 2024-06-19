#Write a python program that takes a list of numbers and returns their sum.
def calculate_sum(numbers):
    total = sum(numbers)
    return total

if __name__ == "__main__":
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = list(map(int, numbers))
    sum_of_numbers = calculate_sum(numbers)
    print("Sum of the numbers:", sum_of_numbers)
    