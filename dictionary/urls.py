from django.urls import path

import dictionary.views

urlpatterns =[

    path('', dictionary.views.home, name="home"),
   
]
