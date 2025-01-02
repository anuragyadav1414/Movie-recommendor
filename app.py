import streamlit as st
import pickle

movies = pickle.load(open("movies_list.pkl", 'rb'))
similarity = pickle.load(open("similarity.pkl", 'rb'))
movies_list = movies['title'].values

st.header("Movie Recommender System")
selected_movie = st.selectbox("Select movie to get recommendation", movies_list)

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    recommended_movies = []
    for i in distances[1:6]:
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

if st.button("Show Recommend"):
    recommended_movies = recommend(selected_movie)
    st.table(recommended_movies)
    # col1, col2, col3, col4, col5 = st.columns(5)
    # with col1:
    #     st.text(recommended_movies[0])
    # with col2:
    #     st.text(recommended_movies[1])
    # with col3:
    #     st.text(recommended_movies[2])
    # with col4:
    #     st.text(recommended_movies[3])
    # with col5:
    #     st.text(recommended_movies[4])