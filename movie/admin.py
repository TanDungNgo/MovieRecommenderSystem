from django.contrib import admin
from .models import User, Movie, Genre, Cast, Director, Keyword, SpokenLanguage, Country, Rating, Review

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role')
    search_fields = ('name', 'email')

admin.site.register(User, UserAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'status')
    list_filter = ('status',)
    search_fields = ('title', 'status')

admin.site.register(Movie, MovieAdmin)

class GenreAdmin(admin.ModelAdmin):
    list_display = ('genre')
    search_fields = ('genre')

admin.site.register(Genre)

class CastAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'gender')
    search_fields = ('character_name')

admin.site.register(Cast)

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('director_name')
    search_fields = ('director_name')

admin.site.register(Director)

class KeywordAdmin(admin.ModelAdmin):
    list_display = ('keyword')
    search_fields = ('keyword')

admin.site.register(Keyword)

class SpokenLanguageAdmin(admin.ModelAdmin):
    list_display = ('language')

admin.site.register(SpokenLanguage)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name')

admin.site.register(Country)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('rating')

admin.site.register(Rating)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review')

admin.site.register(Review)
