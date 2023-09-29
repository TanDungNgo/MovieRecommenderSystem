from django.shortcuts import render

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
