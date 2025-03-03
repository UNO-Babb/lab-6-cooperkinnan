#WordCount.py
#Name:Cooper Kinnan
#Date:3/2/2025
#Assignment:Lab 6

def main():
    # Get the file name from the user
    file_name = input("Enter a file name: ")
    
    # Open the file in read mode
    with open(file_name, 'r') as file:
        # Initialize counters
        line_count = 0
        word_count = 0
        char_count = 0
        
        # Read the file line by line
        for line in file:
            # Update line count
            line_count += 1
            
            # Update word count
            words = line.split()
            word_count += len(words)
            
            # Update character count
            char_count += len(line)
    
    # Print the results
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")

# Run the main function
if __name__ == "__main__":
  main()