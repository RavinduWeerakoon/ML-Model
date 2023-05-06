import pandas as pd
import numpy as np
#Import TfIdfVectorizer from scikit-learn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import pickle
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


df = pd.read_csv('packages.csv')

#Construct a reverse map of indices and product names
indices = pd.Series(df.index, index=df.index)

choices = list(indices.index)
extracted = process.extract("lego", choices, limit=1)
extracted[0][0]


# Function that takes in prompt as input and outputs most similar product
with open("linear_model_plan.pkl", 'rb') as f:
    linear = pickle.load(f)

def rec_lin(user_input,days, linear=linear):
    
    # use fuzzywuzzy to grab the product with name closest to user input
    extracted = process.extract(user_input, choices, limit=1)
    destination = extracted[0][0]
    
    # Get the index of the product that matches the product name
    idx = indices[destination]

    # Get the pairwise similarity scores
    sim_scores = list(enumerate(linear[idx]))

    # Sort the products based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar products
    sim_scores = sim_scores[1:11]

    # Get the product indices
    product_indices = [i[0] for i in sim_scores]

    df_return = df[["Days", "fb id"]].loc[product_indices]

    df_return_list  = df_return[df_return["Days"]==days]["fb id"].to_list()
    
    # Return the top 10 most similar products
    return df_return_list


print(rec_lin("I love watching elephants", 3))