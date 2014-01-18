from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.games.rest.games.forms import GamesPostForm, GamesListGetForm, GamesSingleGetForm
from rememerme.games.rest.exceptions import BadRequestException
from rest_framework.permissions import IsAuthenticated

class GamesListView(APIView):
    permission_classes = (IsAuthenticated,)
    
    '''
       Used for making and viewing friend requests.
    '''            

    def get(self, request):
        '''
            Used to create a new friend request.
        '''
        form = GamesListGetForm(request.QUERY_PARAMS)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()

    def post(self, request):
        '''
            Used to create a new friend request.
        '''
        form = GamesPostForm(request.DATA)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()

class GamesSingleView(APIView):
    permission_classes = (IsAuthenticated,)
    
    def get(self, request, game_id):
        '''
            Used to create a new friend request.
        '''
        form = GamesSingleGetForm({ 'game_id' : game_id })

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()