from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib import messages
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Xác thực thông tin đăng nhập
        try:
            user = MyUser.objects.get(email=email)
            if user.password == password:
                # Tạo một phiên làm việc tùy chỉnh
                request.session['user_id'] = user.id
                return redirect('index')  # Thay 'success_page' bằng URL bạn muốn chuyển hướng đến sau khi đăng nhập thành công
            else:
                # Đăng nhập thất bại, hiển thị thông báo lỗi
                messages.error(request, 'Email or password is incorrect.')
        except MyUser.DoesNotExist:
            # Đăng nhập thất bại, hiển thị thông báo lỗi
            messages.error(request, 'Email or password is incorrect.')

    return render(request, 'signin.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        # Tạo một đối tượng MyUser và lưu vào cơ sở dữ liệu
        user = MyUser(username=username, email=email, password=password)
        user.save()
        
        # Bạn có thể thêm mã xử lý khác ở đây, chẳng hạn như xử lý avatar và role

        # Chuyển hướng người dùng sau khi đăng ký thành công
        return redirect('signin')  # Thay 'success_page' bằng URL bạn muốn chuyển hướng đến sau khi đăng ký

    return render(request, 'signup.html')