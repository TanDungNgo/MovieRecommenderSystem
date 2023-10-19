from django.shortcuts import render, redirect
from movie.models import Movie
from user_page.models import MyUser
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse
from openpyxl import Workbook

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
    return render(request, 'movie_list.html', {'movies': movies})

def user_list(request):
    user_list = MyUser.objects.all()
    return render(request, 'user_list.html', {'user_list': user_list})

def export_to_excel(request, model, fields, filename):
    data = model.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.append(fields)
    for item in data:
        row_data = [getattr(item, field) for field in fields]
        ws.append(row_data)

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{filename}.xlsx"'
    wb.save(response)
    return response

def export_users(request):
    fields = ["username", "email", "password", "role"]
    filename = "user_data"
    return export_to_excel(request, MyUser, fields, filename)

def export_movies(request):
    fields = ["title", "overview", "poster", "movie_duration", "release_date", "status"]
    filename = "movie_data"
    return export_to_excel(request, Movie, fields, filename)

def movie_detail_admin(request, movie_id):
    current_movie = Movie.objects.get(pk=movie_id)
    return render(request, 'movie_detail_admin.html', {'movie': current_movie})