#Write a program that reads data from a CSV file and prints it to the console.
import csv

def read_csv(file_path):
    try:
        with open(file_path, mode='r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            
            # Iterate over each row in the CSV file and print it
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for the path to the CSV file
    file_path = input("Please enter the path to the CSV file: ")
    
    # Call the function to read and print the CSV data
    read_csv(file_path)