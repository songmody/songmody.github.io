from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.index,name='index'),
    path('youtube/', myapp.views.youtube, name='youtube'),
    path('market/', myapp.views.market, name='market'),
    path('signin/', myapp.views.sign, name='sign'),

]
