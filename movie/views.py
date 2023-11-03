from django.shortcuts import render
import pickle
import os
from .models import Movie
import difflib
import requests

import random
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


movies, similarity = load_model()
def search_page(request):
    search = request.GET.get('search')
    recommended_movie = recommend(str(search))

    return render(request, 'search_page.html', 
                  {'movies': recommended_movie})


def index(request):
    # Latest Movies
    # Lấy 8 phim phát hành gần nhất từ cơ sở dữ liệu sắp xếp theo ngày phát hành giảm dần
    latest_movies = Movie.objects.order_by('-release_date')[:8]

    # Chia danh sách 8 phim thành 2 danh sách con, mỗi danh sách con gồm 4 phim
    latest_movies_part1 = latest_movies[:4]
    latest_movies_part2 = latest_movies[4:]
    
    # Lấy danh sách 6 phim Upcoming từ cơ sở dữ liệu
    upcoming_movies = Movie.objects.filter(status='Upcoming')[:6]

    # Chia danh sách 6 phim Upcoming thành 2 danh sách con, mỗi danh sách con gồm 3 phim
    upcoming_movies_part1 = upcoming_movies[:3]
    upcoming_movies_part2 = upcoming_movies[3:]

    context = {
        'latest_movies_part1': latest_movies_part1,
        'latest_movies_part2': latest_movies_part2,
        'upcoming_movies_part1': upcoming_movies_part1,
        'upcoming_movies_part2': upcoming_movies_part2,
    }

    return render(request, 'index.html', context)

def movie_detail(request, movie_id):
    # Lấy ra phim hiện tại
    current_movie = Movie.objects.get(pk=movie_id)

    # Lấy ra tất cả các phim đã phát hành và trộn danh sách ngẫu nhiên
    related_movies = Movie.objects.exclude(pk=movie_id, release_date__lte=current_movie.release_date).order_by('?')[:8]

    # Chia danh sách các phim thành 2 phần
    num_movies_per_section = len(related_movies) // 2
    first_section = related_movies[:num_movies_per_section]
    second_section = related_movies[num_movies_per_section:]

    # Lấy danh sách diễn viên, đạo diễn
    url_credits = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    response = requests.get(url_credits) # Gửi yêu cầu GET đến API
    response.raise_for_status()  # Kiểm tra lỗi trong yêu cầu
    data = response.json() # Chuyển đổi dữ liệu JSON trả về thành một đối tượng Python
    casts = data.get('cast', [])[:8] # Lấy danh sách từ dữ liệu JSON
    directors = [crew for crew in data.get('crew', []) if crew.get('job') == 'Director']

    num_casts_per_row = len(casts) // 2
    first_row = casts[:num_casts_per_row]
    second_row = casts[num_casts_per_row:]

    # Lấy danh sách thể loại
    url_movie = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'
    response = requests.get(url_movie)
    response.raise_for_status()
    data_movie = response.json()
    genres = data_movie.get('genres', [])
    countries = data_movie.get('production_countries', [])


    context = {
        'movie': current_movie,
        'first_section': first_section,
        'second_section': second_section,
        'casts': casts,
        'first_row': first_row,
        'second_row': second_row,
        'genres': genres,
        'countries': countries,
        'directors': directors,
    }

    return render(request, 'movie_detail.html', context)











