from django.shortcuts import render, redirect
from movie.models import Movie
from django.contrib import messages

# Views of Admin
def general(request):
    return render(request, 'general.html')
def button(request):
    return render(request, 'button.html')
def chart(request):
    return render(request, 'chart.html')
def element(request):
    return render(request, 'element.html')
def table(request):
    return render(request, 'table.html')
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

