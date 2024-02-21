from django.urls import path
from .views import userCreateView
from postapi.views import check_database_connection

urlpatterns=[
    path("demo/",userCreateView.as_view(), name='Model-model-api'),
    path('check_database_connection/', check_database_connection, name='check-database-connection'),
]