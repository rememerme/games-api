from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.games.rest.cards.forms import CardForm
from rememerme.games.rest.exceptions import BadRequestException
from rest_framework.permissions import IsAuthenticated


class CardSingleView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, card_id):
        '''
            Used to create a new friend request.
        '''
        form = CardForm({ 'card_id' : card_id })

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()