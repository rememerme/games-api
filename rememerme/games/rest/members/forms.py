'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for friend requests.
    
    Created on Dec 20, 2013

    @author: Andrew Oberlin, Jake Gregg
'''
from django import forms
from rememerme.games.models import Game, GameMember
from rememerme.games.rest.exceptions import IllegalStatusCode, GameNotFound,\
    BadRequestException, GameMemberNotFound
from rememerme.games.serializers import GameMemberSerializer
from uuid import UUID
import uuid
from pycassa.cassandra.ttypes import NotFoundException as CassaNotFoundException
import datetime
import json
from rememerme.games.permissions import GamePermissions
from rememerme.users.client import UserClient, UserClientError

class GameMembersPutForm(forms.Form):
    game_id = forms.CharField(required=True)
    status = forms.IntegerField(required=True)

    def clean(self):
        try:
            self.cleaned_data['game_id'] = str(UUID(self.cleaned_data['game_id']))
        except ValueError:
            raise GameMemberNotFound()
        
        if self.cleaned_data['status'] < 0 or self.cleaned_data['status'] > 2:
            raise IllegalStatusCode()
        
        return self.cleaned_data['status']

    def submit(self, request):
        try:
            # get the game member by the group and user combination
            members = GameMember.filterByGame(self.cleaned_data['game_id'])
            member = None
            for m in members:
                if m.user_id == request.user.pk:
                    member = m
                    break
            if not member:
                raise GameMemberNotFound()
            
            member.status = self.cleaned_data['status']
            member.save()
        except CassaNotFoundException:
            raise GameMemberNotFound()
        return GameMemberSerializer(member).data

'''
    Creates a new game instance.
'''
class GameMembersPostForm(forms.Form):
    game_id = forms.CharField(required=True)
    user_id = forms.CharField(required=True)

    def clean(self):
        '''
            Overriding the clean method to add the default offset and limiting information.
        '''
        try:
            self.cleaned_data['game_id'] = str(UUID(self.cleaned_data['game_id']))
            self.cleaned_data['user_id'] = str(UUID(self.cleaned_data['user_id']))
        except ValueError:
            raise BadRequestException()
        
        return self.cleaned_data
    
    
    def submit(self, request):
        '''
            Submits this form to create the given game.
        '''
        members = GameMember.filterByGame(self.cleaned_data['game_id'])
        member = None
        for m in members:
            if m.user_id == request.user.pk:
                member = m
                break
        if  member:
            raise GameMemberAlreadyExists()
        GameMember()
        return serialized

class GameMembersGetForm(forms.Form):
    game_id = forms.CharField()
    
    def clean(self):
        try:
            self.cleaned_data['game_id'] = str(UUID(self.cleaned_data['game_id']))
        except ValueError:
            raise GameNotFound()
        return self.cleaned_data

    def submit(self, request):
        try:
            game = Game.getByID(self.cleaned_data['game_id'])
            if not GamePermissions.has_object_permission(request, game):
                raise BadRequestException()
        except CassaNotFoundException:
            raise GameNotFound()
        return GameSerializer(game).data


