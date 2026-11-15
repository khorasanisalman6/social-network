from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update/<int:user_id>/', views.UserUpdateView.as_view(), name='update'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('edit_profile/', views.ProfileUpdateView.as_view(), name='edit_profile'),
]