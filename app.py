import streamlit as st
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


@st.cache_data
def load_data():
    movies = pd.read_csv("tmdb_5000_movies.csv")
    credits = pd.read_csv("tmdb_5000_credits.csv")
    movies = movies.merge(credits, on='title')
    movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]

    def extract_names(text):
        return [item['name'] for item in ast.literal_eval(text)]

    def extract_top_cast(text):
        return [item['name'] for i, item in enumerate(ast.literal_eval(text)) if i < 3]

    def extract_director(text):
        for item in ast.literal_eval(text):
            if item['job'] == 'Director':
                return [item['name']]
        return []

    def clean(text_list):
        return [word.replace(" ", "").lower() for word in text_list]

    movies['genres'] = movies['genres'].apply(extract_names).apply(clean)
    movies['keywords'] = movies['keywords'].apply(extract_names).apply(clean)
    movies['cast'] = movies['cast'].apply(extract_top_cast).apply(clean)
    movies['crew'] = movies['crew'].apply(extract_director).apply(clean)
    movies['overview'] = movies['overview'].apply(lambda x: x.split() if isinstance(x, str) else [])
    movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
    movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

    cv = CountVectorizer(max_features=5000, stop_words='english')
    vectors = cv.fit_transform(movies['tags']).toarray()

    similarity = cosine_similarity(vectors)

    return movies, similarity


movies, similarity = load_data()


def recommend(movie_title):
    movie_index = movies[movies['title'] == movie_title].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [movies.iloc[i[0]].title for i in movie_list]


st.title("🎬 Movie Recommender")
st.write("Get movie recommendations based on your favorite!")

movie_list = movies['title'].sort_values().values
selected_movie = st.selectbox("Choose a movie", movie_list)

if st.button("Recommend"):
    try:
        recommendations = recommend(selected_movie)
        st.subheader("Top 5 similar movies:")
        for rec in recommendations:
            st.write("👉", rec)
    except:
        st.error("Movie not found or invalid input.")
