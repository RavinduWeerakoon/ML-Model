#import pandas and numpy
import pickle
import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

dataset = pd.read_csv("dataset.csv")

from ml_model import keyword_extractor

with open('linear_model.pkl', 'rb') as f:
    linear = pickle.load(f)

#Construct a reverse map of indices and product names
indices = pd.Series(dataset.index, index=dataset["Destination"])


choices = list(indices.index)

extracted = process.extract("lego", choices, limit=1)
extracted[0][0]




# Function that takes in prompt as input and outputs most similar product
def rec_lin(user_input, linear=linear):
    
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
    destination_indices = [i[0] for i in sim_scores]

    df_return = dataset[["Destination"]].loc[destination_indices]
    # Return the top 10 most similar products
    return df_return['Destination'].to_list()[:5]


def get_locations(prompt):
    words = " ".join(keyword_extractor(prompt))
    return rec_lin(words)


