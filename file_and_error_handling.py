def file_processor():
    # Get input filename from user
    input_filename = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
            
        print(f"Successfully read from '{input_filename}'")
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create output filename
        output_filename = input_filename.split('.')[0] + '_modified.txt'
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
            
        print(f"Successfully wrote modified content to '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{input_filename}'.")
    except IsADirectoryError:
        print(f"Error: '{input_filename}' is a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode the file '{input_filename}'. It may not be a text file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    file_processor()