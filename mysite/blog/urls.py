from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage),
    path('register', views.register, name='register'),
    path('login', views.login_function, name='login'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('logout', views.Logout, name='logout'),
    path('edit_blog', views.edit_blog, name='edit_blog'),
    path('image_upload', views.image_upload, name='image_upload'),
    path('delete_post', views.delete_post, name='delete_post'),
    path('personal_homepage' , views.personal_homepage, name='personal_homepage'),
    path('add_nickname', views.add_nickname, name='add_nickname'),
    path('add_dob', views.add_dob, name='add_dob')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
