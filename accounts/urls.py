from django.urls import path , reverse_lazy
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('edit_profile/', views.ProfileUpdateView.as_view(), name='edit_profile'),
    path('password-change/', auth_views.PasswordChangeView.as_view(template_name='accounts/password_change_form.html',
                                                                        success_url=reverse_lazy('account:password_change_done')), name='password_change'),
    path(
    'password-change/done/',
    auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_done.html'),name='password_change_done'),

# Password Reset

path(
    'password-reset/',
    auth_views.PasswordResetView.as_view(
        template_name='accounts/password_reset_form.html',
        email_template_name='accounts/password_reset_email.html',
        subject_template_name='accounts/password_reset_subject.txt',
        success_url=reverse_lazy('account:password_reset_done')
    ),
    name='password_reset'
),

path(
    'password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ),
    name='password_reset_done'
),

path(
    'password-reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html',
        success_url=reverse_lazy('account:password_reset_complete')
    ),
    name='password_reset_confirm'
),

path(
    'password-reset/complete/',
    auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ),
    name='password_reset_complete'
),
]