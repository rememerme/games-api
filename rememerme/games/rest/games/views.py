from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.friends.rest.games.forms import GamesPostForm
from rememerme.friends.rest.exceptions import BadRequestException
from rest_framework.permissions import IsAuthenticated

class GamesListView(APIView):
    permission_classes = (IsAuthenticated,)
    
    '''
       Used for making and viewing friend requests.
    '''            

    def post(self, request):
        '''
            Used to create a new friend request.
        '''
        form = GamesPostForm(request.DATA)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()
