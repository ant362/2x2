from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('creat', views.creat, name='creat'),
    path('about', views.about, name='about'),
    path('spis', views.spis, name='spis'),
    path('rasp', views.rasp, name='rasp'),
    path('domz', views.domz, name='domz'),
    path('trenaz', views.trenaz, name='trenaz'),
    path('<int:pk>/del', views.Delete.as_view(), name='delete'),
    path('<int:pk>/edi', views.Edit.as_view(), name='edit'),
    path('<int:pk>/ed_list', views.Ed_list.as_view(), name='ed_list'),
    path('<int:pk>/cr_list', views.Cr_list.as_view(), name='cr_list'),
    #path( '<int:pk>/creat2',views.creat2, name='creat2'),
    path('<int:pk>/zad', views.List.as_view(), name='zad')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                             document_root=settings.MEDIA_ROOT)