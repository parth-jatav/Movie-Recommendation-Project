import streamlit as st
import pickle
import pandas as pd
import requests
import zipfile

# Set the page configuration at the top
st.set_page_config(page_title='Movie Recommender System', layout='wide')


# Load data with caching
@st.cache_data
def load_data():
    with zipfile.ZipFile('similarity.zip', 'r') as zip_ref:
        with zip_ref.open('similarity.pkl') as file:
            similarity = pickle.load(file)
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    return movies, similarity


# Fetch movie poster from API with caching
@st.cache_data
def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=f9b93e48f0111c09389cacb5a8be56dc')
        data = response.json()
        return f'https://image.tmdb.org/t/p/w500/{data["poster_path"]}'
    except:
        return 'https://via.placeholder.com/500x750?text=No+Poster+Available'


# Load movie data and similarity matrix
movies, similarity = load_data()


def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

        recommended_movies = []
        recommended_movies_poster = []
        for i in movie_list:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movies.append(movies.iloc[i[0]].title)
            recommended_movies_poster.append(fetch_poster(movie_id))
        return recommended_movies, recommended_movies_poster
    except:
        return [], []




# Header
st.markdown("""
    <style>
    .header {text-align: center; padding: 20px;}
    </style>
    <div class="header">
    <h1>Movie Recommender System</h1>
    <h4>Find Your Next Favorite Movie!</h4>
    <p>Choose a movie and get recommendations based on your selection.</p>
    </div>
""", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    'Select a Movie:',
    movies['title'].values
)

if st.button('Get Recommendations'):
    with st.spinner('Fetching recommendations...'):
        names, posters = recommend(selected_movie_name)

    if names:
        st.markdown("### Recommended Movies")
        cols = st.columns(5)
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster, use_column_width=True)
                st.subheader(name)
    else:
        st.error("Sorry, no recommendations found.")
