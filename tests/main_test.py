import unittest
import os
import sys
from io import StringIO
from contextlib import redirect_stdout

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import WordLinkGenerator


class WordLinkGeneratorTest(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        self.file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(self.file_path, 'w') as file:
            file.write('This is a test file.\nAnother line with test word.\n')

    def tearDown(self):
        os.remove(self.file_path)
        os.rmdir(self.test_dir)

    def test_find_word_locations(self):
        generator = WordLinkGenerator('test', self.test_dir, None)
        locations = generator.find_word_locations(self.file_path)
        expected_locations = [
            (self.file_path, 1, 'This is a test file.', 10),
            (self.file_path, 2, 'Another line with test word.', 18)
        ]
        self.assertEqual(locations, expected_locations)

    def test_generate_links_output_file(self):
        generator = WordLinkGenerator('test', self.test_dir, 'output.html')
        generator.generate_links()

        self.assertTrue(os.path.isfile('output.html'))

        with open('output.html', 'r') as file:
            output_text = file.read()
            self.assertIn('<html>', output_text)
            self.assertIn('<table>', output_text)
            self.assertIn('<th>File</th>', output_text)
            self.assertIn('<th>Line</th>', output_text)
            self.assertIn('<th>Text</th>', output_text)
            self.assertIn('</table>', output_text)
            self.assertIn('</html>', output_text)

    def test_generate_links_console(self):
        generator = WordLinkGenerator('test', self.test_dir, None)

        # Redirect stdout to capture console output
        captured_output = StringIO()
        with redirect_stdout(captured_output):
            generator.generate_links()

        console_output = captured_output.getvalue()

        expected_output = [
            '+------------------------------+------+------------------------------+',
            '|             File             | Line |             Text             |',
            '+------------------------------+------+------------------------------+',
            '| test_directory/test_file.txt |  1   |     This is a test file.     |',
            '| test_directory/test_file.txt |  2   | Another line with test word. |',
            '+------------------------------+------+------------------------------+'
        ]

        for line in expected_output:
            self.assertIn(line, console_output)


if __name__ == '__main__':
    unittest.main()
