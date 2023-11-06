This is a code to perform intent detection on french language corpus.

### How to use it

- Load a test file test_file_name.csv with two columns "text" and "label". 
- Run the main.py program. There is no argument to parse.
- First, the program will load the model from hugging face library.
- Then, it will be asked to write the path of the test_file_name.csv
- The program will give an output with the accuracy on this test dataset, the speed of the model to predict, and the percentage of "lost luggage" predicted which weren't
