from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static #static utility from settings
urlpatterns = [
    path('', views.task_list_view, name='task_list'),
    path('task/<int:pk>/updated/',views.task_update_view,name='task_update'),
    path('task/<int:pk>/deleted/',views.task_delete_view, name='task_delete'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.register_view, name='register'),
]

# Serves media files during local development
# If you don't include this line in your URLs configuration,
# your browser won't be able to display any images uploaded
# through your Django admin panel or user forms during local testing.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    #The Dynamic Addition > urlpatters +=