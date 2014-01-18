from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #url(r'^rest/v1/games/(?P<game_id>[-\w]+)/round', include('rememerme.games.rest.round.urls')),
    url(r'^rest/v1/games', include('rememerme.games.rest.games.urls')),
)
