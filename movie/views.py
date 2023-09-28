from django.shortcuts import render

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
