from django.urls import path
from . import views

app_name = 'bblog'

urlpatterns = [
    path(r'', views.post_list, name='list'), #全記事表示
    path('<int:pk>/', views.PostDetail, name='detail'), #記事詳細
    path('python/', views.List_Python, name='BigCategory_python'),#大カテゴリー　python
    path('docker/', views.List_docker, name='BigCategory_docker'),#大カテゴリーdocker

]