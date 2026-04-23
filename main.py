import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load datasets
movies = pd.read_csv("movies.csv", encoding='latin1')
credits = pd.read_csv("credits.csv", encoding='latin1')

# Merge datasets
movies = movies.merge(credits, on='title')

# Select required columns
movies = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

# Drop missing values
movies.dropna(inplace=True)

# Convert JSON-like columns
def convert(text):
    try:
        return [i['name'] for i in ast.literal_eval(text)]
    except:
        return []

movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
movies['cast'] = movies['cast'].apply(convert)

# Keep only top 3 cast
movies['cast'] = movies['cast'].apply(lambda x: x[:3])

# Extract director
def fetch_director(text):
    try:
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                return [i['name']]
        return []
    except:
        return []

movies['crew'] = movies['crew'].apply(fetch_director)

# Convert overview to list
movies['overview'] = movies['overview'].apply(lambda x: x.split())

# Remove spaces
def collapse(L):
    return [i.replace(" ", "") for i in L]

movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)

# Combine features
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

# Convert to string
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

# Final dataframe
new_df = movies[['movie_id','title','tags']]

# Vectorization
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()

# Similarity
similarity = cosine_similarity(vectors)

# Recommendation function
def recommend(movie):
    try:
        movie_index = new_df[new_df['title'] == movie].index[0]
        distances = similarity[movie_index]

        movie_list = sorted(list(enumerate(distances)),
                            reverse=True,
                            key=lambda x: x[1])[1:6]

        print("\nRecommended movies:\n")
        for i in movie_list:
            print(new_df.iloc[i[0]].title)

    except:
        print("Movie not found. Please check the name.")

# Test
recommend("Titanic")
  


