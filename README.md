# File Processor with Error Handling

A Python program that reads files, modifies their content, and saves the modified version to a new file with comprehensive error handling.

## Features

- **File Reading**: Safely reads content from any text file
- **Content Modification**: Transforms file content (converts to uppercase)
- **File Writing**: Creates a new file with the modified content
- **Error Handling**: Comprehensive exception handling for:
  - Missing files (FileNotFoundError)
  - Permission issues (PermissionError)
  - Directory inputs (IsADirectoryError)
  - Encoding problems (UnicodeDecodeError)
  - Other unexpected errors

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. No additional dependencies required

## Usage

1. Run the program:
   ```bash
   python file_processor.py
   ```

2. Enter the filename when prompted:
   ```
   Enter the name of the file to read: example.txt
   ```

3. The program will process the file and create a modified version:
   ```
   Successfully read from 'example.txt'
   Successfully wrote modified content to 'example_modified.txt'
   ```

## Example

1. Create a sample file `sample.txt` with content:
   ```
   Hello World!
   This is a test file.
   ```

2. Run the program and enter `sample.txt` when prompted

3. The program will create `sample_modified.txt` with content:
   ```
   HELLO WORLD!
   THIS IS A TEST FILE.
   ```

## Error Handling

The program gracefully handles various error scenarios:

- **File doesn't exist**: "Error: The file 'nonexistent.txt' does not exist."
- **Permission denied**: "Error: Permission denied to read 'protected_file.txt'."
- **Directory provided**: "Error: 'documents' is a directory, not a file."
- **Binary file**: "Error: Could not decode the file 'image.jpg'. It may not be a text file."

## Customization

You can modify the content transformation by changing the `modified_content = content.upper()` line to:

- Convert to lowercase: `content.lower()`
- Capitalize each word: `content.title()`
- Or implement any custom transformation you need.
