from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('sicode',views.sicode,name='sicode'),
    path('additionload',views.additionload,name='additionload'),
    path('additionlogic',views.additionlogic,name='additionlogic')

]