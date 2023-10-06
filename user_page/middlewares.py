
from django.shortcuts import redirect
from django.contrib import messages
class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Kiểm tra xem người dùng đã đăng nhập hay chưa
        if request.user.is_authenticated:
            # Kiểm tra xem người dùng có session 'user_role' không
            if 'user_role' in request.session:
                user_role = request.session['user_role']
                # Kiểm tra xem vai trò của người dùng có phải là admin không
                if user_role != 'admin':
                    # Chặn người dùng truy cập vào các đường dẫn chỉ dành cho admin
                    if request.path.startswith('/admin/'):
                        messages.error(request, 'Log in to your admin account to access')
                        return redirect('/signin/')
        else:
            # Nếu người dùng chưa đăng nhập, chuyển hướng họ đến trang đăng nhập
            if request.path.startswith('/admin/'):
                messages.error(request, 'Log in to your admin account to access')
                return redirect('/signin/')

        response = self.get_response(request)
        return response
