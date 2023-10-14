from django.shortcuts import render, redirect
from movie.models import Movie
from user_page.models import MyUser
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

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
    search_query = request.GET.get('search')
    movie_list = Movie.objects.all()

    if search_query:
        movie_list = movie_list.filter(
            Q(title__icontains=search_query) |  # Tìm theo tiêu đề
            Q(overview__icontains=search_query) |  # Tìm theo tổng quan
            Q(release_date__icontains=search_query)  # Tìm theo ngày phát hành
        )

    items_per_page = 10
    paginator = Paginator(movie_list, items_per_page)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    return render(request, 'movie_list.html', {'movies': movies})

def user_list(request):
    search_query = request.GET.get('search')
    user_list = MyUser.objects.all()

    if search_query:
        user_list = user_list.filter(
            Q(username__icontains=search_query) |  # Tìm theo tên người dùng
            Q(email__icontains=search_query) |     # Tìm theo email
            Q(role__icontains=search_query)        # Tìm theo vai trò
        )

    items_per_page = 10
    paginator = Paginator(user_list, items_per_page)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    return render(request, 'user_list.html', {'user_list': users})

