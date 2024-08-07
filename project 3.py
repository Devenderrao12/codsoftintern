import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(title, 
 movies, tfidf_matrix, cosine_sim):
 

  idx = movies[movies['title'] == title].index[0]


  sim_scores = list(enumerate(cosine_sim[idx]))

  sim_scores = sorted(sim_scores, key=lambda   
 x: x[1], reverse=True)

  movies_indices = [i[0] for i in sim_scores[1:4]]

  return movies['title'].iloc[movies_indices]

movies = pd.DataFrame({
    'title': ['Movie A', 'Movie B', 'Movie C', 'Movie D'],
    'genres': ['Action, Comedy', 'Drama, Romance', 'Comedy, Sci-Fi', 'Action, Adventure']
})

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['genres'])

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

recommendations = get_recommendations('Movie A', movies, tfidf_matrix, cosine_sim)
print(recommendations)