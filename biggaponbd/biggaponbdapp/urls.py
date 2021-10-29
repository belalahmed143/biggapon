from django.urls import path
from .import views
from .views import PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('',views.home, name='home'),
    #path('biggapon/', views.biggapon, name='biggapon'),
    path('userpost/<int:pk>/', PostDetailView.as_view(template_name ='detail.html'), name='post-detail'),
    path('userpost/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('userpost/<int:pk>/delete',PostDeleteView.as_view(), name='post-delete'),
    path('userpost/new/',PostCreateView.as_view(), name='post-create'),
    path('search/', views.searchposts, name='searchposts'),
    path('up_profile/', views.up_profile, name='up_profile'),
    path('toletCategory/<name>/',views.toletCategory, name='toletCategory'),
]
