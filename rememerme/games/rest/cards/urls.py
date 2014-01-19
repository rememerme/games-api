from django.conf.urls import patterns, url

from rememerme.games.rest.games import views

urlpatterns = patterns('',
    url(r'^/(?P<card_id>[-\w]+)/?', views.CardSingleView.as_view()),
)
