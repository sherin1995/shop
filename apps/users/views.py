from django.shortcuts import render

# Create your views here.
from django.views import View


class RegisterView(View):
    """
    提供注册界面
    """

    def get(self, request):
        return render(request, 'register.html')
