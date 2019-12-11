from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, default='prof.jpg')
    age = models.IntegerField(null=True)
    contact = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    county = models.ForeignKey('Traditonsongs', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'profiles'
        ordering = ['name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_profiles(cls, searchTerm):
        profiles = cls.objects.filter(name__icontains=searchTerm)
        return profiles

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(name=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()


class Traditonsongs(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    image = models.ImageField(upload_to='trad_images/', blank=True)

    class Meta:
        db_table = 'traditiontrads'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def search_trad(cls, searchTerm):
        trad = cls.objects.filter(name__icontains=searchTerm)
        return trad

    @classmethod
    def search_by_title(cls, search_term):
        trad = cls.objects.filter(name__icontains=search_term)
        return trad


class Songs(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'songses'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_song(cls, searchTerm):
        song = cls.objects.filter(name__icontains=searchTerm)
        return song


class LatestContact(models.Model):
    name = models.CharField(max_length=250)
    contact = models.CharField(max_length=250)
    description = models.TextField()

    class Meta:
        db_table = 'e_contacts'
        ordering = ['-name']

    def __repr__(self):
        return f'{self.name}'

    @classmethod
    def search_late(cls, searchTerm):
        late = cls.objects.filter(name__icontains=searchTerm)
        return late


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=250)
    tag = models.CharField(max_length=250)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    trad = models.ForeignKey('Traditonsongs', on_delete=models.CASCADE, related_name='trad', default=1)

    class Meta:
        db_table = 'posts'
        ordering = ['-title']

    def __repr__(self):
        return f'{self.title}'

    @classmethod
    def search_posts(cls, searchTerm):
        posts = cls.objects.filter(title__icontains=searchTerm)
        return posts

