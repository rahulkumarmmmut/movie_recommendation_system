import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlYTI4NDQ3NWFlMmI4YjJkZmE3ZWE3ZTQ4MDI0NTY2MCIsIm5iZiI6MTcyMjQ0ODIyNy4xNzA4NDcsInN1YiI6IjY2YWE3N2Y5ZGRiNzQ5ZGFkOGJkMGM2NCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.tewpJRjgyw4zbpxsPI44z0_f7_c99dJ9fP8NsA7Yeis"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from API
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))
st.title("Movie :blue[Recommendation] System :sunglasses:")
st.divider()

selected_movie_name = st.selectbox(
    "How would you like to be contacted?",
    movies['title'].values)

if st.button("Recommend"):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0], width=200)
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1], width=200)

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2], width=200)
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3], width=200)
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4], width=200)
