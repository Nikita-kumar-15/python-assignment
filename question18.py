#Write a python program that checks if two strings are anagrams of each other.
from collections import Counter

def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    
    count_str1 = Counter(str1)
    count_str2 = Counter(str2)
    
    if count_str1 == count_str2:
        return True
    else:
        return False

if __name__ == "__main__":
    str1 = input("Enter the first string: ").strip()
    str2 = input("Enter the second string: ").strip()
    
    if are_anagrams(str1, str2):
        print(f"'{str1}' and '{str2}' are anagrams.")
    else:
        print(f"'{str1}' and '{str2}' are not anagrams.")