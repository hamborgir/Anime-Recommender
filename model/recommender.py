import pandas as pd
import numpy as np

import os, sys

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def find_anime_index(data : pd.DataFrame, id : int):
    idx = data.index[data['anime_id'] == id].to_list()

    if not idx:
        raise ValueError("Couldn't find given id or name.")
        
    return idx[0]

def find_anime_id(data : pd.DataFrame, title : str, first : bool = True):
    if title is None:
        raise ValueError("Title cannot be empty string.")

    id = data.loc[data['Clean Title'].str.contains(title.lower()), "anime_id"].to_list()
        
    if first:
        return id[0]
    else:
        return id   
    

# def load_similarity_mat():
#     df = pd.read_csv("./preprocessed_anime_data.csv")

    
    pass

class Recommender:
    
    __similarity = None
    __data = None

    def __init__(self):
        self.__similarity = np.load("./similarity_matrix.npy")
        self.__data = pd.read_csv("preprocessed_anime_data.csv")
        
    def __init__(self, similarity_mat : np.ndarray, data : pd.DataFrame):
        self.__similarity = similarity_mat
        self.__data = data

    def recommend(self, data :pd.DataFrame, mat : np.ndarray, id : int = None, count = 10, title : str = None):
        if id is None:
            if title is None:
                raise ValueError("If id is ommited, anime title must be included.")
            id = find_anime_id(data, title)

        idx = find_anime_index(data, id = id)
        
        return pd.DataFrame({"id" : data.loc[np.argsort(mat[idx])[:-count-1:-1], "anime_id"],
                             "title" : data.loc[np.argsort(mat[idx])[:-count-1:-1], "Name"], 
                             "similarity":np.sort(mat[idx])[:-count-1:-1]},).reset_index(drop=True)


    
        

if __name__ == "__main__":
    os.getcwd()

np.__dict__