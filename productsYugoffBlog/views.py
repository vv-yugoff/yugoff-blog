from django.shortcuts import render
from .models import PortfolioItem
from .models import SkillsItem

# Create your views here.

def index(request):
    # portfolio = PortfolioItem.objects.all()
    context = {
        'title': 'Yugoff - Programmer, CV Engineer',
        'skills': SkillsItem.objects.all(),
        'portfolio': PortfolioItem.objects.all(),
    }
    return render(request, 'productsYugoffBlog/index.html', context)

# def index(request):
#     context = {
#         'title': 'Yugoff - Programmer, ML Engineer',
        
#         'portfolio': [
#             {
#                 'image': 'static/site-yugoff-blog/image/logo-new.png',
#                 'alt': 'Рус Групп ИЛАН',
#                 'href': 'https://ilanbusiness.ru/',
#                 'title': '«Рус Групп «ИЛАН»',
#                 'types': 'ilanbusiness.ru'
#             },
#             {
#                 'image': 'static/site-yugoff-blog/image/o-nas.png',
#                 'alt': 'РСК ИЛАН',
#                 'href': 'http://rsc-ilan.ru/',
#                 'title': '«Ресурсоснабжающая компания «ИЛАН»',
#                 'types': 'rsc-ilan.ru'
#             }
#         ]
#     }
#     return render(request, 'productsYugoffBlog/index.html', context)
