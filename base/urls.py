from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name = 'home'),
    path('addsticker/<str:pk>/<str:username>',views.addSticker, name = 'addSticker'),
    path('substicker/<str:pk>/<str:username>',views.subSticker, name = 'subSticker'),
    path('login/', views.loginURL, name = 'login'),
    path('register/', views.register, name = 'register'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('userfinder/', views.getUser, name = 'userfinder'),
    path('profile/<str:username>', views.userPublicProfile, name = 'userPublicProfile'),
    path('exchange/<str:username>', views.getExchangeStickers, name = 'exchange'),
    path('stickerfinder/', views.getSticker, name = 'stickerfinder'),
    path('bulkimport/', views.importBulk, name = 'bulk'),
    path('exchangerequest/<str:username>', views.exchangeRequest, name = 'exchangerequest'),
    path('lobby/', views.lobbyChat, name='lobby')

]


