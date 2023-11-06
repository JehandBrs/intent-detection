This is a code to perform intent detection on french language corpus.

### How to use it

- Load a test file test_file_name.csv with two columns "text" and "label". 
- Run the main.py program. There is no argument to add.
- First, the program will load the model from hugging face library, it takes 1-2 minutes.
- Then, the program will ask to write as input the path to the test_file_name.csv file
- The program will give an output with the accuracy on this test dataset, the speed of the model to predict, and the False Positive Rate for the "lost luggage" category
