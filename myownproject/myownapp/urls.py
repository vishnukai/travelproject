from . import views
from django.urls import path
#myproject
urlpatterns = [


    path('',views.demo,name='demo'),

    # path('addition/',views.addition,name='addition')
]
