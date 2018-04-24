from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.urlresolvers import reverse
from django.views import generic
from communities.models import Community, 


# Create your views here.
class CreateCommunity(LoginRequiredMixin, generic.CreateView):
    fields = ('name', 'description')
    model = Community

class SingleCommunity(generic.DetailView):
    model = Community

class ListCommunities(generic.ListView):
    model = Community
