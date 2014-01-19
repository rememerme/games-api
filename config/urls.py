from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^rest/v1/games/(?P<game_id>[-\w]+)/rounds', include('rememerme.games.rest.rounds.urls')),
    url(r'^rest/v1/games/(?P<game_id>[-\w]+)/members', include('rememerme.games.rest.members.urls')),
    url(r'^rest/v1/games', include('rememerme.games.rest.games.urls')),
    url(r'^rest/v1/cards', include('rememerme.games.rest.cards.urls')),
)
