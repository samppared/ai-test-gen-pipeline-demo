from functions import *

# First initial promt to ask ChatGPT for tests
def get_tests(given_file, key):
  # Setup variables to be used
  test_file = "unit_tests.py"
  promt = "Please provide unittests for the following python code\n"
  promt += "In your awnser, please just give the code, nothing more\n\n"
  promt += "\n".join(fail_str(file_read(given_file)))
  setup = "You are a skilled engineer assistant"

  # Get code from ChatGPT and write the output to a file
  file_write(test_file, get_chatgpt(key,setup,promt).content)
  # Clean the given code, ie remove the "```python" etc from it
  file_write(test_file, clean_code(test_file,given_file))

get_tests(sys.argv[1], sys.argv[2])