from django.shortcuts import render
from django.views import View


class Main(View):
    """выводит главную страницу сайта"""
    def get(self, request):
        return render(request, 'main/main.html')

class About(View):
    """выводит описание сайта"""
    def get(self, request):
        return render(request, 'main/about.html')
