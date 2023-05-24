# Wordlink Examples

Wordlink is a command-line tool that allows you to search for a specific term within text files and generate an HTML file containing clickable links to the matched occurrences.

## Usage

Assuming you have a directory structure like this:

```
- wordlink/
  - main.py
- examples/
  - testdir/
    - a.txt
    - b.txt
    - c.txt
- results.html
```

You can use the following command to run wordlink:

```bash
python3 -m wordlink examples/testdir orange -o results.html
```

This command will search for the term "orange" within the text files located in the `examples/testdir` directory. It will generate an output file named `results.html` containing clickable links to the matched occurrences.

After running the command, the program will process the files, generate the output HTML file, and display a message indicating that the output was written to the specified file:

```
Output written to results.html
```

You can then open the `results.html` file in a web browser to view the generated links.

Note: Make sure to run the command from the same directory where the `__main__.py` file is located, and ensure that the `examples/testdir` directory and the `results.html` file are present in the appropriate locations.
