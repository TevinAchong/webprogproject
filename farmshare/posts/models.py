from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings
import misaka
from communities.models import Community
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

class Post(models.Model):
    user = models.ForeignKey(User, related_name = 'posts')
    date_created = models.DateTimeField(auto_now = True)
    content = models.TextField()
    content_html = models.TextField(editable = False)
    community = models.ForeignKey(Community, related_name = 'posts', null = True, blank = True)

    def __str__(self):
        return self.content
    
    def save(self, *args, **kwargs):
        self.content_html = misaka.html(self.content)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('posts : single', kwargs = {'username' : self.user.username, 'pk' : self.pk})

    class Meta:
        ordering = ['-date_created']
        unique_together = ['user', 'content']
    



