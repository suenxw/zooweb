
from django.urls import path
from django.contrib import admin
from rango import views
from django.conf.urls import url
from django.conf.urls import include

app_name = 'rango'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('category/<slug:category_name_slug>/search', views.SearchAnimalView.as_view(), name='search_animal'),

    url(r'^add_category/$',views.add_category,name='add_category'),
    path('category/<slug:category_name_slug>/add_animal/', views.add_animal, name='add_animal'),
    path('restricted/', views.restricted, name='restricted'),

    path('register_profile/', views.RegisterProfileView.as_view(), name='register_profile'),
    path('profile/<username>/', views.ProfileView.as_view(), name='profile'),
    path('profiles/', views.ListProfilesView.as_view(), name='list_profiles'),
    path('aniaml_profile/<animal_name>/', views.AnimalProfileView.as_view(), name='animal_profile'),
    path('like_animal/', views.LikeAnimalView.as_view(), name='like_animal'),
    path('aniaml_profile/<animal_name>/<username>/post_comment', views.CommentPostView, name='post_comment'),

]
