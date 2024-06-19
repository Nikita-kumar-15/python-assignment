#Write a program in python that converts a string into a list of its characters
def string_to_list(input_string):
    return list(input_string)

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    char_list = string_to_list(input_string)
    print("List of characters:", char_list)