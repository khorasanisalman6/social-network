from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('',views.HomePage.as_view(),name='home'),
    path('create/',views.PostCreateView.as_view(),name='create'),
    path('detail/<int:pk>/<slug:slug>/',views.PostDetailView.as_view(),name='detail'),
    path('update/<int:pk>/',views.PostUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.PostDeleteView.as_view(),name='delete'),
]