# Printing data files
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
# General libraries
import re, os, string
import pandas as pd
import pickle
TOP_KEYWORDS = 10

# Scikit-learn importings
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import word_tokenize




with open('keyword_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('keyword_features.pkl', 'rb') as f:
    feature_names = pickle.load(f)
def sort_coo(coo_matrix):
    """Sort a dict with highest score"""
    tuples = zip(coo_matrix.col, coo_matrix.data)
    return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)


def get_stopwords_list(stop_file_path):
    """load stop words """
    
    with open(stop_file_path, 'r', encoding="utf-8") as f:
        stopwords = f.readlines()
        stop_set = set(m.strip() for m in stopwords)
        return list(frozenset(stop_set))

def extract_topn_from_vector(feature_names, sorted_items, topn=10):
    """get the feature names and tf-idf score of top n items"""
    
    #use only topn items from vector
    sorted_items = sorted_items[:topn]

    score_vals = []
    feature_vals = []
    
    # word index and corresponding tf-idf score
    for idx, score in sorted_items:
        
        #keep track of feature name and its corresponding score
        score_vals.append(round(score, 3))
        feature_vals.append(feature_names[idx])

    #create a tuples of feature, score
    results= {}
    for idx in range(len(feature_vals)):
        results[feature_vals[idx]]=score_vals[idx]
    
    return results

def get_keywords(vectorizer, feature_names, doc):
    """Return top k keywords from a doc using TF-IDF method"""

    #generate tf-idf for the given document
    tf_idf_vector = vectorizer.transform([doc])
    
    #sort the tf-idf vectors by descending order of scores
    sorted_items=sort_coo(tf_idf_vector.tocoo())

    #extract only TOP_K_KEYWORDS
    keywords=extract_topn_from_vector(feature_names,sorted_items,TOP_KEYWORDS)
    
    return list(keywords.keys())


def remove_stopwords(prompt):

    tokens = word_tokenize(prompt.lower())


    english_stopwords = get_stopwords_list('stopwords.txt')
    tokens_wo_stopwords = [t for t in tokens if t not in english_stopwords]
    return  " ".join(tokens_wo_stopwords)




def keyword_extractor(user_prompt):
    user_prompt = remove_stopwords(user_prompt)
    return get_keywords(vectorizer, feature_names, user_prompt)