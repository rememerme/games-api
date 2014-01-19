'''
    This file holds all of the forms for the cleaning and validation of
    the parameters being used for friend requests.
    
    Created on Dec 20, 2013

    @author: Andrew Oberlin, Jake Gregg
'''
from django import forms
from rememerme.cards.models import PhraseCard
from rememerme.games.rest.exceptions import PhraseCardNotFound
from rememerme.cards.serializers import PhraseCardSerializer    
from uuid import UUID
from pycassa.cassandra.ttypes import NotFoundException as CassaNotFoundException

class CardForm(forms.Form):
    card_id = forms.CharField()
    
    def clean(self):
        try:
            self.cleaned_data['card_id'] = str(UUID(self.cleaned_data['card_id']))
        except ValueError:
            raise PhraseCardNotFound()
        return self.cleaned_data

    def submit(self, request):
        try:
            card = PhraseCard.getByID(self.cleaned_data['card_id'])
        except CassaNotFoundException:
            raise PhraseCardNotFound()
        return PhraseCardSerializer(card).data
        
        
        
        

