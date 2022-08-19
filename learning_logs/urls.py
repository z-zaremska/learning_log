"""Definiuje wzorce adresów URL dla learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    #Main site
    path('', views.index, name='index'),
    #Topics site
    path('topics', views.topics, name='topics'),
    path('topics/(<int:topic_id>)', views.topic, name='topic'),
    #New topic formula
    path('new_topic', views.new_topic, name='new_topic'),
    #New entry formula
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #Edit entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]