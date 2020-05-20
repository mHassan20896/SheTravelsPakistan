from django.db import models

# Create your models here.
class Blog(models.Model):
    article = models.TextField()
    title = models.CharField( max_length=200)
    image = models.ImageField(upload_to='images/blog')
    published_date = models.DateField()

    def __str__(self):
        return self.title

class TripCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/comments',blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.name

class Destination(models.Model):

    DESTINATION_CHOICES = (('Pakistan','Pakistan'),('International','International'))

    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/destinations')
    text = models.TextField()
    destination = models.CharField(max_length=20, choices=DESTINATION_CHOICES)


    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(TripCategory, on_delete=models.CASCADE)
    starting_Quote = models.IntegerField()
    image = models.ImageField(upload_to='images/packages')
    facilities = models.ManyToManyField(Facility,blank=False)

    def __str__(self):
        return self.title

class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.BigIntegerField()
    packages = models.ManyToManyField(Package,blank=True)

    def __str__(self):
        return self.name

class Requirement(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Career(models.Model):
    title = models.CharField(max_length=50)
    requirements = models.ManyToManyField(Requirement,blank=False)

    def __str__(self):
        return self.title

class TravelGuide(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    #image = models.ImageField(upload_to="travel-guide")
    intro = models.TextField(max_length=400)
    city_tour_in = models.CharField(max_length=50)
    tour_name = models.CharField(max_length=50)
    languages = models.CharField(max_length=100)
    tour_duration = models.IntegerField()
    meeting_place = models.CharField(max_length=50)
    cost_per_person = models.IntegerField()
    tour_include = models.TextField(max_length=400)
    tour_doesnt_include = models.TextField(max_length=400)
    what_you_do_during_tour = models.TextField(max_length=400)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    intro = models.TextField()
    image = models.ImageField(upload_to='images/members')

    def __str__(self):
        return self.name
    