from django.shortcuts import render
from .models import Article

class HomeView:
    def get(self, request):
        list_articles = Article.objects.all()
        context = {"liste_articles": list_articles}
        return render(request, "index.html", context)
