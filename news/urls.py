from xml.etree.ElementInclude import include

from django.urls import path
#имортируем созданное нами представление
from .views import NewsList, NewsDetail, NewsSearch, NewsCreate, NewsUpdate, NewsDelete, author_now, CategoryListView, \
    subscribe

urlpatterns = [
    path('', NewsList.as_view(), name='post_list'),
    path('search/', NewsSearch.as_view(), name='search'),
    path('<int:pk>/', NewsDetail.as_view(), name='post_detail'),
    path('create/', NewsCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('articles/create/', NewsCreate.as_view(), name='post_create'),
    path('articles/<int:pk>/edit/', NewsUpdate.as_view(), name='post_edit'),
    path('articles/<int:pk>/delete/', NewsDelete.as_view(), name='post_delete'),
    path('author_now/', author_now, name='author_now'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
    path('accounts/', include('allauth.urls'))
]
