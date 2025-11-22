import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US')
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# App title and description
st.markdown("<h1 style='text-align: center; color: #FF5733;'>Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Discover your next favorite movie with just a click!</p>", unsafe_allow_html=True)

# Movie selection dropdown
selected_movie_name = st.selectbox(
    'Select a movie you like:',
    movies['title'].values,
    help="Choose a movie to get recommendations based on your choice."
)

# Recommendation button
if st.button('Recommend'):
    with st.spinner('Finding recommendations...'):
        names, posters = recommend(selected_movie_name)

    # Display recommended movies in a responsive grid
    st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Recommended Movies</h3>", unsafe_allow_html=True)
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.image(poster, use_container_width=True)
            st.markdown(f"<p style='text-align: center;'>{name}</p>", unsafe_allow_html=True)

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)