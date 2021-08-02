# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:47:09 2021

@author: Amarnadh Tadi
"""

import pandas as pd
entertainment=pd.read_csv(r"C:\Users\Amarnadh Tadi\Desktop\datascience\assign7\Entertainment.csv", encoding = 'utf8')
entertainment.shape # shape
entertainment.columns
entertainment.Category # genre columns

entertainment["Category"].isnull().sum()
##removies of reviews whose values are not in between -9 to 9
ent = entertainment[~(entertainment['Reviews'] >9)] 
ent1=ent[~(ent['Reviews'] <-9)] 
#term frequencey- inverse document frequncy

from sklearn.feature_extraction.text import TfidfVectorizer
tdidf=TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(entertainment.Category)   
tfidf_matrix.shape 

from sklearn.metrics.pairwise import linear_kernel

# Computing the cosine similarity on Tfidf matrix
cosine_sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)

# creating a mapping of entertainment title to index number 
ent1_index = pd.Series(ent1.index, index = ent1['Titles']).drop_duplicates()

ent1_id = ent1_index["Toy Story (1995)"]
ent1_id
def get_recommendations(Title, topN):    
    # topN = 10
    # Getting the movie index using its title 
    ent1_id = ent1_index[Title]
    
    # Getting the pair wise similarity score for all the anime's with that 
    # anime
    cosine_scores = list(enumerate(cosine_sim_matrix[ent1_id]))
    
    # Sorting the cosine_similarity scores based on scores 
    cosine_scores = sorted(cosine_scores, key=lambda x:x[1], reverse = True)
    
    # Get the scores of top N most similar movies 
    cosine_scores_N = cosine_scores[0:topN+1]
    
    # Getting the movie index 
    ent1_idx  =  [i[0] for i in cosine_scores_N]
    ent1_scores =  [i[1] for i in cosine_scores_N]
    
    # Similar movies and scores
    ent1_similar_show = pd.DataFrame(columns=["Title", "Score"])
    ent1_similar_show["Title"] = ent1.loc[ent1_idx, "Titles"]
    ent1_similar_show["Score"] = ent1_scores
    ent1_similar_show.reset_index(inplace = True)  
    # anime_similar_show.drop(["index"], axis=1, inplace=True)
    print (ent1_similar_show)
    # return (anime_similar_show)

    
# Enter your title and number of title to be recommended 
get_recommendations("Toy Story (1995)", topN = 1)

