# polish_notation
Simple function to calculate result of a given expression
in Reverse Polish Notation.

# Get started

1. Create and activate a Python 3 virtual environment (if you don't want to install pytest globally)
2. Install the requirements with `pip install -r requirements.txt` from the project root
   - You might need to run `pip3` instead depending on your default system python
3. Run tests with `pytest --verbose` from the project root (one expected failure -- see notes
   for bonus recursive implementation in `src/rpn.py`)

The code does not currently provide a command line interface. You can run it interactively as follows:

1. Start a Python (3) console in the project root, e.g. `python` or `python3`
2. Run `from src.rpn import calculate`
3. Now you can call the function, e.g. `calculate("1 2 +")`

# Room for improvement

- Handle more operators (`sin`, `sqrt`, `log` etc.)
- More informative exception handling for invalid notation
