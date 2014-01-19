from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.games.rest.members.forms import GameMembersPostForm, GameMembersGetForm, GameMembersPutForm
from rememerme.games.rest.exceptions import BadRequestException
from rest_framework.permissions import IsAuthenticated

class GameMembersView(APIView):
    permission_classes = (IsAuthenticated,) 
    
    '''
       Used for making and viewing friend requests.
    '''            

    def get(self, request, game_id):
        '''
            Used to create a new friend request.
        '''
        query = { q for q in request.QUERY_PARAMS }
        query['game_id'] = game_id
        form = GameMembersGetForm(query)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()

    def post(self, request, game_id):
        '''
            Used to create a new friend request.
        '''
        query = { q for q in request.DATA }
        query['game_id'] = game_id
        form = GameMembersPostForm(query)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()
        
    def put(self, request, game_id):
        '''
            Change the state of a game member in the game.
        '''
        query = { q for q in request.DATA }
        query['game_id'] = game_id
        form = GameMembersPutForm(query)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()