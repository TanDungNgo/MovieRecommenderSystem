from django.shortcuts import render
import pickle
import os
from .models import Movie
import difflib

def load_model():
    pkl_folder = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'MovieRecommenderSystem/model')

    movie_list_pkl = os.path.join(pkl_folder, 'movie_list.pkl')
    similarity_pkl = os.path.join(pkl_folder, 'similarity.pkl')

    movies = pickle.load(open(movie_list_pkl,'rb'))
    similarity = pickle.load(open(similarity_pkl,'rb'))

    return movies, similarity
    
def recommend(movie_name):
    list_of_all_titles = movies['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match = find_close_match[0]
    index = movies[movies['title'] == close_match].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie = []

    for i in distances[1:13]:
        movie_id = movies.iloc[i[0]].movie_id
        movie = Movie.objects.get(id=movie_id)
        recommended_movie.append(movie)

    return recommended_movie
# Views of User
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def blog_detail(request):
    return render(request, 'blog_detail.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')
def movie_detail(request):
    return render(request, 'movie_detail.html')

movies, similarity = load_model()
def search_page(request):
    search = request.GET.get('search')
    recommended_movie = recommend(str(search))

    return render(request, 'search_page.html', 
                  {'movies': recommended_movie})