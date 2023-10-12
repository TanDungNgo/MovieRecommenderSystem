from django.db import models
from user_page.models import MyUser

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.URLField(blank=True, null=True)
    overview = models.TextField()
    movie_duration = models.TextField()
    release_date = models.DateField()
    status = models.TextField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name

class Movie_Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.genre

class Cast(models.Model):
    character_name = models.CharField(max_length=100)
    gender = models.BooleanField()
    Role = models.TextField()

    def __str__(self):
        return self.character_name
    
class Movie_Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cast = models.ForeignKey(Cast, on_delete=models.CASCADE)
    def __str__(self):
        return self.cast

class Director(models.Model):
    director_name = models.CharField(max_length=100)

    def __str__(self):
        return self.director_name
    
class Movie_Director(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.director

class Keyword(models.Model):
    keyword = models.TextField()

    def __str__(self):
        return self.keyword
    
class Movie_Keyword(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword

class SpokenLanguage(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.TextField()

    def __str__(self):
        return self.language

class Country(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name

class Rating(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=1)

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}: {self.rating}'

class Review(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

    
