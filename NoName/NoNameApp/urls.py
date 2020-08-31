from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('vote/', views.vote, name='vote'),
    path('signup/', views.signup, name='signup')
]
