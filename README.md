This is a code to perform intent detection on french language corpus.

### How to use it
1) Load the test file test_file_name.csv. It must have two columns : "text" and "label". 
2) Run the main.py program. There is no argument to add on the CLI.
3) First, the program will load the model from hugging face library, it takes a few minutes.
4) Then, the program will ask to write as input the path to the test_file_name.csv file.
5) The program will give an output with
   - the accuracy on this test dataset
   - the model speed to predict (per sentence)
   - the False Positive Rate for the "lost luggage" category
