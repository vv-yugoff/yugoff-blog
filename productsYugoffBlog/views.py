from django.shortcuts import render
from .models import PortfolioItem
from .models import SkillsItem
from .models import Data
from .serializer import DataSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def getData(request):
    app = Data.objects.all()
    serializer = DataSerializer(app, many=True)
    return Response(serializer.data)

def index(request):
    # portfolio = PortfolioItem.objects.all()
    context = {
        'title': 'Yugoff - Programmer, ML Engineer',
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
