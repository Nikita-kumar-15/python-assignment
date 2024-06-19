#Write a python program that returns the minimum and maximum values in a list of numbers.
def find_min_max(numbers):
    if not numbers:
        return None, None
    
    min_value = min(numbers)
    max_value = max(numbers)
    return min_value, max_value

if __name__ == "__main__":
    numbers = [3, 7, 1, 9, 5, 2, 8]
    min_val, max_val = find_min_max(numbers)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")