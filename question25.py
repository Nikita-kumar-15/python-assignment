#Write a program that copies the contents of one text file to another.
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as dest:
                dest.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")

if __name__ == "__main__":
    source_file = input("Enter the path of the source text file: ")
    destination_file = input("Enter the path of the destination text file: ")
    
    copy_file(source_file, destination_file)
    