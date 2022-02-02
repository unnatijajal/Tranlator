from django.urls import path

import dictionary.views

urlpatterns =[

    path('', dictionary.views.home, name="home"),
    # path('form', dictionary.views.change),
    path('/', dictionary.views.talk, name="btn")
]