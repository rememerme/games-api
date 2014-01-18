'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for friend requests.
    
    Created on Dec 20, 2013

    @author: Andrew Oberlin, Jake Gregg
'''
from django import forms
from rememerme.games.models import Game
from rememerme.games.rest.exceptions import GameNotFoundException
from rememerme.games.serializers import GamesSerializer
from uuid import UUID
from pycassa.cassandra.ttypes import NotFoundException as CassaNotFoundException
import datetime

'''
    Creates a new game instance.
'''
class GamesPostForm(forms.Form):
    user_id = forms.CharField(required=True)

    '''
        Overriding the clean method to add the default offset and limiting information.
    '''
    def clean(self):
        return self.cleaned_data
    
    '''
        Submits this form to create the given game.
    '''
    def submit(self, request):
        pass

class GamesSingleGetForm(forms.Form):
    def clean(self):
        return self.cleaned_data

    def submit(self, request):
        pass




