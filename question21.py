#Write a python program that counts the occurrences of a specific element in a list.
def count_occurrences(input_list, element):
    count = 0
    for item in input_list:
        if item == element:
            count += 1
    return count

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 1, 1, 5, 1]
    target_element = 2
    occurrences = count_occurrences(numbers, target_element)
    print(f"Number of occurrences of {target_element}: {occurrences}")