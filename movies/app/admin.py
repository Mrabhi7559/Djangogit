from django.contrib import admin
from app.models import Movie
from django.http import HttpResponse

admin.site.register(Movie)