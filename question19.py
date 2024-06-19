#Write a python program that removes all punctuation from a given string.
import string

def remove_punctuation(input_string):
    punctuations = set(string.punctuation)
    result_string = ""
    
    for char in input_string:
        if char not in punctuations:
            result_string += char
    
    return result_string

if __name__ == "__main__":
    input_string = input("Enter a string with punctuation: ")
    cleaned_string = remove_punctuation(input_string)
    print("String without punctuation:", cleaned_string)