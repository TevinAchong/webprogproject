from django.db import models
from django.utils.text import slugify #Removing characters that are not alphanumeric
import misaka #Link embedding
from django.contrib.auth import get_user_model
from django import template
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
User = get_user_model()
register = template.Library() #Custom template tags

class Community(models.Model):
    name = models.CharField(max_length = 255, unique = True)
    slug = models.SlugField(allow_unicode = True, unique = True)
    description = models.TextField(blank = True, default = '')
    description_html = models.TextField(editable = False, default = '', blank = True)
    members = models.ManyToManyField(User, through = 'CommunityMember')

    def __str__ (self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        print(self.slug, "*********")
        return reverse("communities:single", kwargs={"slug":self.slug})

    class Meta:
        ordering = ['name']




class CommunityMember(models.Model):
    community = models.ForeignKey(Community, related_name = 'memberships')
    user = models.ForeignKey(User, related_name = 'user_communities')

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('community', 'user')

    


