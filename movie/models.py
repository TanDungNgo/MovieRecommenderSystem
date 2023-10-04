from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='img/')
    overview = models.TextField()
    movie_duration = models.DurationField()
    release_date = models.DateField()
    status = models.TextField()

    def __str__(self):
        return self.title

class Genre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.genre

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    character_name = models.CharField(max_length=100)
    gender = models.BooleanField()
    Role = models.TextField()

    def __str__(self):
        return self.character_name

class Director(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director_name = models.CharField(max_length=100)

    def __str__(self):
        return self.director_name

class Keyword(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    keyword = models.TextField()

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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=1, decimal_places=1)

    def __str__(self):
        return f'{self.user.name} - {self.movie.title}: {self.rating}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    review = models.TextField()

    def __str__(self):
        return f'{self.user.name} - {self.movie.title}'

    
