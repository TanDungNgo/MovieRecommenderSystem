from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib import messages
from django.contrib.auth import logout
def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        # Kiểm tra xem email và password đã được nhập
        if email and password:
            try:
                user = MyUser.objects.get(email=email)
                if user.password == password:
                    # Tạo một phiên làm việc tùy chỉnh
                    request.session['user_id'] = user.id
                    request.session['user_username'] = user.username
                    # request.session['user_avatar'] = user.avatar.url
                    request.session['user_role'] = user.role
                    # Điều hướng tới trang tương ứng
                    if user.role == 'user':
                        # Điều hướng sang trang user
                        return redirect('index')
                    if user.role == 'admin':
                        # Điều hướng sang trang admin
                       return redirect('/admin/')
                    
                else:
                    # Đăng nhập thất bại, hiển thị thông báo lỗi
                    messages.error(request, 'Email or password is incorrect.')
            except MyUser.DoesNotExist:
                # Đăng nhập thất bại, hiển thị thông báo lỗi
                messages.error(request, 'Email or password is incorrect.')
        else:
            # Người dùng chưa nhập thông tin, hiển thị thông báo lỗi
            messages.error(request, 'Please enter both email and password.')

    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        # Kiểm tra xem các trường đã điền đầy đủ hay chưa và hiển thị thông báo lỗi nếu cần
        if not username:
            messages.error(request, 'Username is required.')
        if not email:
            messages.error(request, 'Email is required.')
        if not password:
            messages.error(request, 'Password is required.')

        # Kiểm tra xem có thông báo lỗi hay không
        if messages.get_messages(request):
            return render(request, 'signup.html')

        # Nếu không có lỗi, tạo một đối tượng MyUser và lưu vào cơ sở dữ liệu
        user = MyUser(username=username, email=email, password=password, role = 'user')
        user.save()

        # Bạn có thể thêm mã xử lý khác ở đây, chẳng hạn như xử lý avatar và role

        # Chuyển hướng người dùng sau khi đăng ký thành công
        return redirect('signin')  # Thay 'success_page' bằng URL bạn muốn chuyển hướng đến sau khi đăng ký

    return render(request, 'signup.html')


def signout(request):
    logout(request)
    return redirect('signin')  # Điều hướng sau khi đăng xuất (thay 'login' bằng URL của trang đăng nhập của bạn)