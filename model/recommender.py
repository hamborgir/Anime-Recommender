import pandas as pd
import numpy as np

import os, sys

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

class Recommender:
    """
    
    """
        
    def __init__(self, similarity_mat : str = None, data : str = None):
        if similarity_mat is None and data is None:
            similarity_mat = "./model/similarity_matrix.npy"
            data = "./model/preprocessed_anime_data.csv"

        self.__mat = np.load(similarity_mat)
        self.__data = pd.read_csv(data)

        self.__dict = {"id" : "anime_id", "title" : "Name", "cleaned title" : "Clean Title"}
        self.__publ_col = ["anime_id", "Name", "Score", "Genres", "Synopsis", "Type", "Studios", "Rating", "Favorites", "Image URL"]
        # TODOS: replace column access to __data to be ruled with __dict

    def recommend(self, id : int = None, count = 10, title : str = None):
        """
        
        """

        count = count + 2

        if id is None:
            if title is None:
                raise ValueError("If anime id is ommited, anime title must be included.")
            id = self.find_anime_id(title)

        idx = self.find_anime_index(id = id)
        rec_idx = np.argsort(self.__mat[idx])[-2:-count:-1]

        df = self.data.loc[rec_idx, self.__publ_col].reset_index(drop=True)
        df = pd.concat([pd.DataFrame({"similarity":np.sort(self.__mat[idx])[-2:-count:-1]}), df], axis=1)
        
        return df
        # return pd.DataFrame({"id" : self.data.loc[np.argsort(self.__mat[idx])[:-count-1:-1], "anime_id"],
        #                      "title" : self.data.loc[np.argsort(self.__mat[idx])[:-count-1:-1], "Name"], 
        #                      "similarity":np.sort(self.__mat[idx])[:-count-1:-1]},).reset_index(drop=True)

    def find_anime_index(self, id : int):
        idx = self.__data.index[self.__data['anime_id'] == id].to_list()

        if not idx:
            raise ValueError("Couldn't find given id.")
            
        return idx[0]

    def find_anime_id(self, title : str, first : bool = True):
        if title is None:
            raise ValueError("Title cannot be empty string.")

        id = self.__data.loc[self.__data['Clean Title'].str.contains(title.lower()), "anime_id"].to_list()
            
        if first: return id[0]
        else: return id

    @property
    def data(self):
        return self.__data[self.__publ_col]
        

if __name__ == "__main__":
    print()
    pass