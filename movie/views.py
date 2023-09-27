from django.shortcuts import render

# Views of User
def index(request):
    return render(request, 'User/index.html')
def about(request):
    return render(request, 'User/about.html')
def blog(request):
    return render(request, 'User/blog.html')
def blog_detail(request):
    return render(request, 'User/blog_detail.html')
def services(request):
    return render(request, 'User/services.html')
def contact(request):
    return render(request, 'User/contact.html')

# Views of Admin
def general(request):
    return render(request, 'Admin/general.html')
def blank(request):
    return render(request, 'Admin/blank.html')
def button(request):
    return render(request, 'Admin/button.html')
def chart(request):
    return render(request, 'Admin/chart.html')
def element(request):
    return render(request, 'Admin/element.html')
def form(request):
    return render(request, 'Admin/form.html')
def table(request):
    return render(request, 'Admin/table.html')
def typography(request):
    return render(request, 'Admin/typography.html')
def widget(request):
    return render(request, 'Admin/widget.html')
def signin(request):
    return render(request, 'Admin/signin.html')
def signup(request):
    return render(request, 'Admin/signup.html')
