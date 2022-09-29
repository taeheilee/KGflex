from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name='KGflex'
urlpatterns = [
    path('anime-details', views.KGflexList.as_view(), name='anime-details'),
    path('index', views.KGflex_list, name='list'),
    path('free/<int:pk>/', views.KGflexDetail.as_view(), name='detail'),
    path('create_KGflex/', views.KGflexCreate.as_view(),name='KGflex_create'),
    path('delete_KGflex/<int:pk>/', views.KGflexDelete,name='KGflex_delete'),
    path('update_KGflex/<int:pk>/', views.KGflexUpdate.as_view(),name='KGflex_update'),

    path('notice', views.notice_list.as_view(), name='notice_list'),
    path('notice/<int:pk>/', views.NoticeDetail.as_view(), name='notice_detail'),
    
    
    
    
    
    path('KDrama', views.KDrama_list.as_view(), name='KDrama_list'),
    path('KDrama/<int:pk>/', views.KDramaDetail.as_view(), name='KDrama_detail'),







    path('entertainment', views.entertainment_list.as_view(), name='entertainment_list'),
    path('entertainment/<int:pk>/', views.entertainmentDetail.as_view(), name='entertainment_detail'),





    path('KMovie', views.KMovie_list.as_view(), name='KMovie_list'),
    path('KMovie/<int:pk>/', views.KMovieDetail.as_view(), name='KMovie_detail'),
 



    path('UMovie', views.UMovie_list.as_view(), name='UMovie_list'),
    path('UMovie/<int:pk>/', views.UMovieDetail.as_view(), name='UMovie_detail'),






    path('signup', views.signup , name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='KGflex/login.html'), name='login'),
    
]
