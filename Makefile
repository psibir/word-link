# Variables
PYTHON = python3
PIP = pip3

# Default target
.PHONY: all
all: install test

# Install dependencies
.PHONY: install
install:
	$(PIP) install -r requirements.txt

# Run tests
.PHONY: test
test:
	$(PYTHON) -m unittest discover -s tests

# Clean up generated files
.PHONY: clean
clean:
	rm -rf build dist *.egg-info
	rm -rf __pycache__

# Create a distribution package
.PHONY: package
package: clean
	$(PYTHON) setup.py sdist bdist_wheel

# Publish the package to PyPI
.PHONY: publish
publish: package
	$(PYTHON) -m twine upload dist/*

# Run the wordlink program
.PHONY: run
run:
	$(PYTHON) -m wordlink

# Add more rules and commands as needed
