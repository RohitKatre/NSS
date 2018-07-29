from django.shortcuts import render
from .models import *
from django.views.generic import CreateView, DetailView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from .forms import *




class IndexView(ListView):
    model = Notification
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        notification = Notification.objects.all()[:6]
        event = Evenet.objects.all()[:6]
        context['notification'] = notification
        context['event'] = event
        return context


class UserCreateView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = "user_app/signup.html"
    success_url = "/"


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "user_app/user_list"


# class UserDeleteView(LoginRequiredMixin, DeleteView):
#     model = User