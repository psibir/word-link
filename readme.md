## word-link

A Word Link Generator that searches for a given term in multiple text files within a specified directory and generates links to the matched occurrences. It provides two output options: an HTML file with clickable links or a console display using a formatted table.

### Prerequisites

- Python 3.x
- `argparse` library
- `fuzzysearch` library
- `prettytable` library

### Installation

1. Clone the repository or download the script file.
2. Install the required libraries by running the following command:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the script using the following command:

```bash
python main.py <search_term> <search_directory> [-o OUTPUT_FILE]
```

- `<search_term>`: The term to search for within the text files.
- `<search_directory>`: The directory to search for text files.
- `-o OUTPUT_FILE` or `--output_file OUTPUT_FILE`: (Optional) Specify the output file name to save the results as an HTML file. If not provided, the results will be displayed in the console using a formatted table.

**Examples:**

1. Search for the term "example" in the current directory and display the results in the console:

   ```bash
   python main.py example .
   ```

2. Search for the term "example" in the directory "documents" and save the results as an HTML file named "output.html":

   ```bash
   python word_link_generator.py example documents -o output.html
   ```

### Output

The tool generates two types of output depending on the presence of the output file option:

1. **HTML Output File:** If an output file is specified using the `-o` or `--output_file` option, the tool generates an HTML file with clickable links. Each link represents a matched occurrence in a specific file and line. The output file contains a table with columns for the file name, line number, and corresponding text.

2. **Console Display:** If no output file is provided, the tool displays the results in the console using a formatted table. The console output includes columns for the file name, line number, and corresponding text.

### Limitations

- The tool searches for the specified term within all text files (`.txt`) in the given directory and its subdirectories. It does not support searching within other file formats.
- The maximum Levenshtein distance for finding near matches is set to 1. This can be adjusted by modifying the `max_l_dist` parameter in the `find_near_matches` function call within the `find_word_locations` method.

### License

This code is provided under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and use it according to your needs.
