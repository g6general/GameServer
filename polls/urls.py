from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('info/<int:id>/', views.getAccountInfo, name='getAccountInfo'),
    path('add/', views.addAccount, name='addAccount'),
    path('save/', views.saveAccount, name='saveAccount'),
    path('remove/<int:id>/', views.removeAccount, name='removeAccount'),
    path('statistics/', views.showStatistics, name='showStatistics'),
    path('analytics/<int:id>/', views.showAnalytics, name='showAnalytics'),
    path('token/', views.getToken, name='getToken')
]