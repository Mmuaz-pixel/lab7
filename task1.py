import os
import argparse

def search_file(directory, filename, case_sensitive=True, multiple_files=False):
    """
    Recursively searches for a file in a directory and its subdirectories.
    
    Parameters:
    - directory (str): The path to the directory where the search starts.
    - filename (str): The name of the file to search for.
    - case_sensitive (bool): If False, performs a case-insensitive search.
    - multiple_files (bool): If True, searches for multiple instances of the file.
    
    Returns:
    - List of paths where the file was found, or an empty list if not found.
    """
    found_paths = []

    # Handle case sensitivity
    target_file = filename if case_sensitive else filename.lower()

    try:
        for root, _, files in os.walk(directory):
            for file in files:
                current_file = file if case_sensitive else file.lower()
                if current_file == target_file:
                    found_paths.append(os.path.join(root, file))
                    if not multiple_files:
                        return found_paths

    except Exception as e:
        print(f"Error: {e}")
        return []

    return found_paths


def main():
    parser = argparse.ArgumentParser(description="Recursive File Search")
    parser.add_argument("directory", type=str, help="Directory path to search in")
    parser.add_argument("filename", type=str, help="File name to search for")
    parser.add_argument("--case-insensitive", action="store_true", help="Perform a case-insensitive search")
    parser.add_argument("--multiple", action="store_true", help="Search for multiple files")
    
    args = parser.parse_args()

    directory = args.directory
    filename = args.filename
    case_sensitive = not args.case_insensitive
    multiple_files = args.multiple

    # Search for the file
    result = search_file(directory, filename, case_sensitive, multiple_files)
    
    # Display results
    if result:
        for path in result:
            print(f"File found: {path}")
    else:
        print("File not found.")

if __name__ == "__main__":
    main()
