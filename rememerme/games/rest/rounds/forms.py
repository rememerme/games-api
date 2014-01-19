'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for friend requests received.
    
    Created on Dec 20, 2013

    @author: Andrew Oberlin, Jake Gregg
'''
from django import forms
from rememerme.games.models import Game, Round, GameMember
from rememerme.cards.models import PhraseCard
from rememerme.games.rest.exceptions import NoCurrentRound,\
    GameNotFound, GameAlreadyStarted
from rememerme.games.serializers import RoundSerializer
from uuid import UUID
from pycassa.cassandra.ttypes import NotFoundException as CassaNotFoundException
import datetime
import random

'''
    Gets all friend requests recieved and returns them to the user.

    @return: A list of requests matching the query with the given offset/limit
'''        
class StartGameForm(forms.Form):
    game_id = forms.CharField(required=True)
    deck_id = forms.CharField(required=True)
    
    def clean(self):
        try:
            self.cleaned_data['game_id'] = str(UUID(self.cleaned_data['game_id']))
            self.cleaned_data['deck_id'] = str(UUID(self.cleaned_data['deck_id']))
        except ValueError:
            raise GameNotFound()
        return self.cleaned_data
    
    
    '''
        Submits the form and returns the friend requests received for the user.
    '''
    def submit(self, request):
        try:
            game = Game.getByID(self.cleaned_data['game_id'])
            if game.current_round_id:
                raise GameAlreadyStarted()
        except CassaNotFoundException:
            raise GameNotFound()
        
        # select randomly from the game members
        game_members = GameMember.filterByGame(game.game_id)
        selector = random.choice(game_members)
        
        now = datetime.datetime.now()
        
        round = Round(selector_id=selector.game_member_id, phrase_card_id=PhraseCard.getRandom(self.cleaned_data['deck_id']).phrase_card_id,
            game_id=game.game_id, date_created=now, last_modified=now)
        
        round.save()
        
        game.deck = self.cleaned_data['deck_id']
        game.save()

        return RoundSerializer(round).data
    
'''
    Accepts a friend request for a user.

    @return: Validation of accepting the request.
'''
class RoundForm(forms.Form):
    game_id = forms.CharField(required=True)
    
    def clean(self):
        cleaned_data = super(RoundForm, self).clean()
        try:
            cleaned_data['game_id'] = str(UUID(cleaned_data['game_id']))
        except ValueError:
            raise GameNotFound()
        return cleaned_data
    
    def submit(self, request):
        game_id = self.cleaned_data['game_id']
        
        try:
            game = Game.getByID(game_id)
        except CassaNotFoundException:
            raise GameNotFound()
        
        try:
            if not game.current_round_id:
                raise NoCurrentRound()
            round = Round.getByID(game.current_round_id)
        except CassaNotFoundException:
            raise NoCurrentRound()
        
        return RoundSerializer(round).data
        

'''
    Denies a friend request for the user.

    @return: confirmation that the request was denied.
'''
class NominationsGetForm(forms.Form):
    user_id = forms.CharField(required=True)
    
    def clean(self):
        try:
            self.cleaned_data['user_id'] = str(UUID(self.cleaned_data['user_id']))
            return self.cleaned_data
        except ValueError:
            raise GameNotFound()
    
    '''
        Submits the form to deny the friend request.
    '''
    def submit(self, request):
        pass
    

'''
    Denies a friend request for the user.

    @return: confirmation that the request was denied.
'''
class NominationsPostForm(forms.Form):
    user_id = forms.CharField(required=True)
    
    def clean(self):
        try:
            self.cleaned_data['user_id'] = str(UUID(self.cleaned_data['user_id']))
            return self.cleaned_data
        except ValueError:
            raise GameNotFound()
    
    '''
        Submits the form to deny the friend request.
    '''
    def submit(self, request):
        pass
    
'''
    Denies a friend request for the user.

    @return: confirmation that the request was denied.
'''
class SelectionForm(forms.Form):
    user_id = forms.CharField(required=True)
    
    def clean(self):
        try:
            self.cleaned_data['user_id'] = str(UUID(self.cleaned_data['user_id']))
            return self.cleaned_data
        except ValueError:
            raise GameNotFound()
    
    '''
        Submits the form to deny the friend request.
    '''
    def submit(self, request):
        pass
    
        
