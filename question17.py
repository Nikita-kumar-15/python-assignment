#Write a program in python that converts a given string to title case (first letter of each word capitalized).
def convert_to_title_case(input_string):
    title_case_string = input_string.title()
    return title_case_string

if __name__ == "__main__":
    input_string = input("Please enter a string: ")
    title_case_string = convert_to_title_case(input_string)
    print("Title Case:", title_case_string)