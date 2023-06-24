from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name='home'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('Login',views.Login,name='Login'),
    path('Logout',views.Logout,name='Logout'),
    path('VotePage',views.VotePage,name='VotePage'),
    path('VoteDone',views.VoteDone,name='VoteDone'),
    path('Search',views.Search,name='Search'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)