import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    res = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=acb7d647d5d4cdc0f43e5ab2461032f8&language=en-US'.format(movie_id))
    data = res.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        # fetch poster form api
        recommend_movies_poster.append(fetch_poster(movie_id))


    return recommend_movies, recommend_movies_poster

movies_list = pickle.load(open('./movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('./similarity.pkl','rb'))

st.title('Movie recommendation system')

selected_movie_name = st.selectbox(
    'List of movies',
    movies
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(3)
    for idx, col in enumerate(cols):
        if idx < len(names):
            with col:
                st.text(names[idx])
                st.image(posters[idx])
