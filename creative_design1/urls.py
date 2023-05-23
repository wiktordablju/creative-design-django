"""Definiuje wzorce adresow url dla creativedesign1"""

from django.urls import path

from . import views

app_name = 'creative_design1'
urlpatterns = [
    # Strona glowna
    path('', views.index, name='index'),
    # Wyswietlanie wszystkich tematow
    path('topics/', views.topics, name='topics'),
    # Szczegolowa strona dla kazdego tematu
    path('topics/(<int:topic_id>)/', views.topic, name='topic'),
    # Strona przeznaczona do dodawania nowego tematu
    path('new_topic/', views.new_topic, name='new_topic'),
    # Strona do dodawania nowych wpisow
    path('new_entry/<int:topic_id>)/', views.new_entry, name='new_entry'),
    # Strona przeznaczona do edycji wpisu
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry')

]
