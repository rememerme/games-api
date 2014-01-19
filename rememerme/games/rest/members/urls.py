from django.conf.urls import patterns, url

from rememerme.games.rest.members import views

urlpatterns = patterns('',
    url(r'^/(?P<game_id>[-\w]+)/members/?', views.GameMembersView.as_view())
)
