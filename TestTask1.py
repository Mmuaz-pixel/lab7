import unittest
import os
from task1 import search_file  # Adjust if the script is saved under a different name

class TestSearchFile(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setup a sample directory structure for testing
        os.makedirs("test_dir/subdir", exist_ok=True)
        with open("test_dir/test_file.txt", "w") as f:
            f.write("This is a test file.")
        with open("test_dir/subdir/test_file.txt", "w") as f:
            f.write("This is another test file.")
        with open("test_dir/subdir/another_file.TXT", "w") as f:
            f.write("This is another file.")

    @classmethod
    def tearDownClass(cls):
        # Clean up files after tests
        import shutil
        shutil.rmtree("test_dir")

    def test_file_found(self):
        # Test for file found in a single directory
        result = search_file("test_dir", "test_file.txt")
        self.assertEqual(len(result), 1)
        self.assertIn("test_dir/test_file.txt", result[0])

    def test_file_found_in_subdir(self):
        # Test for file found in a subdirectory
        result = search_file("test_dir", "test_file.txt", multiple_files=True)
        self.assertEqual(len(result), 2)
        self.assertIn("test_dir/test_file.txt", result[0])
        self.assertIn("test_dir/subdir/test_file.txt", result[1])

    def test_case_insensitive_search(self):
        # Test for case-insensitive search
        result = search_file("test_dir", "ANOTHER_FILE.txt", case_sensitive=False)
        self.assertEqual(len(result), 1)
        self.assertIn("test_dir/subdir/another_file.TXT", result[0])

    def test_multiple_files(self):
        # Test for searching multiple occurrences
        result = search_file("test_dir", "test_file.txt", multiple_files=True)
        self.assertEqual(len(result), 2)

    def test_file_not_found(self):
        # Test when file is not found
        result = search_file("test_dir", "non_existent_file.txt")
        self.assertEqual(result, [])

    def test_invalid_directory(self):
        # Test with a non-existent directory
        result = search_file("invalid_dir", "test_file.txt")
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
