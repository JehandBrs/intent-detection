import argparse
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
import pandas as pd 
import transformers
from transformers import AutoTokenizer, AutoModel
import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer, util
import time
PATH_TO_DATA = 'data/'

if __name__=='__main__':
    print('Preparation of the model starts')
    # Load model from HuggingFace 
    model = SentenceTransformer('sentence-transformers/LaBSE')
    
    # Load data
    df_train = pd.read_csv(PATH_TO_DATA+'intent-detection-train.csv')
    # Store data into a list
    X = df_train['text'].tolist()
    X_embedded = model.encode(sentences=X)
    
    
    print('Preparation Done. \n')
    input_user = input("Please, give a sentence, or a path to a csv file to test the model on : ")
    
    # Time the procedure
    s_start = time.time()
    
    # Load data or read the sentence from input
    if input_user==(PATH_TO_DATA+'intent-detection-train.csv'):
        print('This path is the train dataset, we can\'t test our model on it')
    elif '.csv' in input_user:
        try :
            df_test = pd.read_csv(input_user)
            X_test = df_test['text'].tolist()
            single_sentence = False
        except : 
            print('No file for the path :', input_user)
    else:
        X_test = [input_user]
        single_sentence = True
        
    # Embed the input to the vectorized representation 
    X_embedded_test = model.encode(X_test)
    
    # Now we compute the cosine similarity with the training dataset
    results = [
        [util.pytorch_cos_sim(x1, x2).numpy()[0,0] for j, x2 in enumerate(X_embedded)]
        for i, x1 in enumerate(X_embedded_test)
        ]
    
    # We get the index of the most similar sentence from our train dataset, for each input
    indexes = [np.argmax(r) for r in results]

    # We then get the corresponding line in the dataframe
    predicted_similar_sentences = df.loc[indexes]
    
    # We compute the accuracy of our model on the test set
    accuracy = (predicted_similar_sentences['label'].to_numpy()==df_test['label'].to_numpy()).sum()/len(df_test)*100
    
    # Build the confusion matrix to get the results for lost luggage label
    conf_matrix = multilabel_confusion_matrix(
        y_true = df_test['label'].to_numpy(), 
        y_pred = predicted_similar_sentences['label'].to_numpy(), 
        labels = ['lost_luggage'],
        )[0]

    
    # Print the results of our models
    s_end = time.time()
    
    # Accuracy
    print('Accuracy for this test set is :', round(accuracy, 2), '%')
    # False negative are the special case we want to avoid 
    print('Percentage of sentences classified as "lost luggage" which weren\'t :', round(conf_matrix[1,0]/conf_matrix.sum(), 2) , '%')
    # Show rapidity of our model
    print('Computed ', len(X_test), ' results in ', round(s_end-s_start, 2), 's ('+str(round((s_end-s_start)/len(X), 4))+'s/sentence)')

    
    
    
    
    
