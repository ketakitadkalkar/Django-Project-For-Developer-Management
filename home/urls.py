from django.conf.urls import url
from django.urls import path

from home import views
from .views import register
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'home'

urlpatterns = [
    path('home/', views.index, name='homepage'),
    path('register', register, name='register'),
    path('', views.login, name='login'),
    # path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    url(r'posts/$', views.index1, name='ShowDevelopers'),
    # path('developer/create',views.AuthorCreate.as_view()),
    path('developer', views.get_data, name='developer'),
    # path('edit/', views.edit, name='edit_developer'),
    # path('edit/', views.edit1, name='edit-developer'),
    url(r'^edit/(?P<id>[0-9]+)/$', views.edit),
    url(r'^delete/(?P<id>[0-9]+)/$', views.delete_dev),
    #url('delete/',views.delete_dev),
    path('search', views.search_dev, name='search'),
    path('forgot', views.forget, name='forgot'),
    # path('developer/<int:pk>/update/', views.AuthorUpdate.as_view(), name='developer-update'),
    # path('developer/<int:pk>/delete/', views.AuthorDelete.as_view(), name='developer-delete'),
]
