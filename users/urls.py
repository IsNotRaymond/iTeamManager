from django.contrib.auth import views
from django.contrib.auth.decorators import login_required

from .views import SignUpView, ActivateAccount
from django.urls import path

urlpatterns = [
    path('login/', views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('password_change/', login_required(views.PasswordChangeView.as_view(), login_url='login'),
         name='password_change'),

    path('password_change/done/', login_required(views.PasswordChangeDoneView.as_view(), login_url='login'),
         name='password_change_done'),

    path('password_reset/', views.PasswordResetView.as_view(html_email_template_name=
                                                            'registration/password_reset_email.html'),
         name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]
