from django.shortcuts import render, redirect
from urllib.request import urlopen
from datetime import datetime
from .models import Article
from .forms import BookForm
import json




def index(request):


    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():

            attname = 'id'
            num_articles = Article.objects.count()
            last_article = Article.objects.order_by('id')[num_articles - 1]
            id_num = getattr(last_article, attname)

            isbn = form.get_isbn()

            Article(id=(id_num + 1), author=form.get_name(), title=form.get_title(), content=form.get_review(),  image=getimage(isbn), isbn=isbn).save()
            return redirect('/books/')
    else:
        form = BookForm()

    context = {
        'current_date': datetime.now(),
        'title': 'Home',
        'form': form,
    }
    return render(request, 'index.html', context)


def about(request):
    context = {
        'current_date': datetime.now(),
        'title': 'About',
    }
    return render(request, 'about.html', context)

def books(request):
    populate_db()
    articles = get_articles()
    context = {
        'articles': articles,
        'current_date': datetime.now(),
        'title': 'Books',

    }
    return render(request, 'books.html', context)


def get_articles():
    result = Article.objects.all()
    return result

def populate_db():
    if Article.objects.count() == 0:
        title1 = 'Invisible Man'
        title2 = 'Slaughterhouse-Five'
        title3 = 'The Outsiders (novel)'

        Article(id = 1, author='Ravi', title= title1, content='first review', image=getimage(title1)).save()
        Article(id = 2, author='Ravi', title= title2, content='second review', image=getimage(title2)).save()
        Article(id = 3, author='Ravi', title= title3, content='third review', image=getimage(title3)).save()

def getimage(isbn):
    url = "https://www.googleapis.com/books/v1/volumes?q=" + isbn
    # try:
    response = urlopen(url)
    #except HTTPError as e:
    #    print "Error: {mess}".format(mess=e)
    #    return "Error: {mess}".format(mess=e)
    j = json.load(response)
    link = j["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"]
    return link
