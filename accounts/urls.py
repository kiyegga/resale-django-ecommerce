from django.urls import path
# from django.contrib.auth import login
# from . import views
from  django.contrib.auth import views as auth_view
from .views import signup


app_name = 'accounts'

urlpatterns = [
    path('signup/', signup, name='signup')
    # path('login/', auth_view.LoginView.as_view(), name='login'),
    # path('password_change/', auth_view.PasswordChangeView.as_view(),
    #      name='logipassword_changen'),
    # path('password_change/done/', auth_view.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),
    # path('password_reset/', auth_view.PasswordResetView.as_view(),
    #      name='password_reset'),
    # path('password_reset/done/', auth_view.PasswordResetDoneView.as_view(),
    #      name='password_reset_done'),


#     accounts/reset/<uidb64 > / < token > / [name = 'password_reset_confirm']
#     accounts/reset/done / [name= 'password_reset_complete']
]
