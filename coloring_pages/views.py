from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import *
from .utils import *
from .forms import *
from .serializers import *


# Create your views here.

class RegisterUserForm(DataMixin, CreateView):
    form_class = Register
    template_name = 'coloring_pages/registeruser.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUserForm(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'coloring_pages/loginuser.html'

    def get_success_url(self):
        return reverse_lazy('home')


class ColoringPageHome(DataMixin, ListView):
    paginate_by = 6
    model = Coloring_page
    template_name = 'coloring_pages/ListColoringPage.html'
    context_object_name = 'Coloring_pages'


class CategoryColoringPage(DataMixin, ListView):
    model = Tema
    template_name = 'coloring_pages/ListTema.html'
    context_object_name = 'Tems'

    def get_queryset(self):
        return Tema.objects.filter(cat__slug=self.kwargs['category'])


class ListColoringPageOfTema(DataMixin, ListView):
    model = Coloring_page
    template_name = 'coloring_pages/ListColoringPageOfTema.html'
    context_object_name = 'Coloring_pages'

    def get_queryset(self):
        return Coloring_page.objects.filter(tema__slug=self.kwargs['tema'])


class ShowPage(DataMixin, DetailView):
    model = Coloring_page
    template_name = 'coloring_pages/ShowPage.html'
    slug_url_kwarg = 'page_slug'
    context_object_name = 'Post'


def logout_user(request):
    logout(request)
    return redirect('home')


class ColoringPageApiView(generics.ListCreateAPIView):
    queryset = Coloring_page.objects.all()
    serializer_class = ColoringPageSerializar
    permission_classes = [IsAuthenticatedOrReadOnly]

class TemaApiView(generics.ListCreateAPIView):
    queryset = Tema.objects.all()
    serializer_class = TemaSerializar
    permission_classes = [IsAuthenticatedOrReadOnly]

class CategoryApiView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializar
    permission_classes = [IsAuthenticatedOrReadOnly]

