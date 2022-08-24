from django.contrib import admin
from django.urls import path
from App_F import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_Registration, name='registration'),
    path('login', views.user_Login, name='login'),
    path('contact', views.contact, name='contact'),
    path('percentage', views.percentage, name='percentage'),
    


    path('createpost', views.create_Post, name='createpost'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('delete/<int:post_id>', views.delete_Post, name='delete'),
    path('editpost/<int:post_id>', views.edit_Post, name='editpost'),
    path('update/<str:id>', views.post_Update, name='update'),
    path('logout', views.logout, name='logout'),
    path('index', views.index_Post, name='index'),
    path('calculator', views.calculator, name='calculator'),
    path('showpost/<int:post_id>', views.show_Post, name='showpost'),
    path('search', views.search_Post, name='search'),

]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)