from django.urls import path
from .views import index, login_user, submit_login, logout_user, list_estoque
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('', index),
    path('login/', login_user),
    path('login/submit', submit_login),
    path('logout/', logout_user),
    path('estoque/', list_estoque),
    path('', RedirectView.as_view(url='login/')),


    #    path('estoque_geral', estoque_geral)
]
