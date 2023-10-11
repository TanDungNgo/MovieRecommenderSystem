from django.shortcuts import render, redirect
from movie.models import Movie
from user_page.models import MyUser
from django.contrib import messages

# Views of Admin
def general(request):
    total_movies = Movie.objects.count()
    total_users = MyUser.objects.filter(role='user').count()
    return render(request, 'general.html', {'total_movies': total_movies, 'total_users': total_users})

def create_movie(request):
    if request.method == 'POST':
        title = request.POST['title']
        overview = request.POST['overview']
        movie_duration = request.POST['movie_duration']
        release_date = request.POST['release_date']
        status = request.POST['status']
        
        if 'file-input' in request.FILES:
            poster = request.FILES['file-input']
        else:
            poster = None

        movie = Movie(
            title=title,
            overview=overview,
            movie_duration=movie_duration,
            release_date=release_date,
            status=status,
            poster=poster
        )
        movie.save()

        messages.success(request, 'Phim đã được tạo thành công!')
        return redirect('/admin/list/') 
    return render(request, 'create_movie.html') 

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movie_list': movies})

def user_list(request):
    users = MyUser.objects.all()
    return render(request, 'user_list.html', {'user_list': users})

