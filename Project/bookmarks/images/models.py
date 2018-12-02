from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse


class Image(models.Model):
    listing_choices= (
        ('Rent', 'Rent'),
        ('Sell','Sell'),
        ('Buy','Buy'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,
                             related_name='images_created')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    #url = models.URLField()
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    street_address = models.CharField(blank=False,db_index=True,max_length=200)
    city = models.CharField(blank=False,db_index=True,max_length=50)
    zipcode = models.CharField(max_length=5, blank=False)
    price = models.PositiveIntegerField(blank=True,null=True)
    listing_type = models.CharField(max_length=4, choices=listing_choices,default='Rent')
    amenities=models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)
    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    def __str__(self):
        return 'Post {}'.format(self.title)    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Image, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('images:detail', args=[self.id, self.slug])
