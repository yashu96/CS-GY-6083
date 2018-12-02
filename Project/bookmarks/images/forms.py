from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify
from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ('title','listing_type','image', 'street_address','city','zipcode','price','description','amenities')
        

    def clean_url(self):
        print(self.image)
        url = self.cleaned_data['image']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.rsplit('.', 1)[1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL does not match valid image extensions.')
        return url

    def save(self, force_insert=False, force_update=False, commit=True):
        image = super(ImageCreateForm, self).save(commit=False)
        image_name = '{}'.format(slugify(image.title))
        # download image from the given URL
        # response = request.urlopen(image_url)
        # image.image.save(image_name,
        #                   ContentFile(image),
        #                   save=False)

        if commit:
            image.save()
        return image
