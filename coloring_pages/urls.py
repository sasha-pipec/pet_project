from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ColoringPageHome.as_view(), name='home'),
    path('<slug:category>/', CategoryColoringPage.as_view(), name='Category'),
    path('post/<slug:tema>/', ListColoringPageOfTema.as_view(), name='Tema'),
    path('about/<slug:page_slug>/', ShowPage.as_view(), name='Detail'),
    path('/register/', RegisterUserForm.as_view(), name='register'),
    path('/login/', LoginUserForm.as_view(), name='login'),
    path('/logout/', logout_user, name='logout'),



    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/coloring_page', ColoringPageApiView.as_view()),
    path('api/v1/tema', TemaApiView.as_view()),
    path('api/v1/category', CategoryApiView.as_view()),

]
