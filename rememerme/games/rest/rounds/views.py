from rest_framework.views import APIView
from rest_framework.response import Response
from rememerme.friends.rest.received.forms import ReceivedGetListForm, ReceivedPutForm, ReceivedDeleteForm
from rememerme.friends.rest.exceptions import BadRequestException
from rest_framework.permissions import IsAuthenticated

class ReceivedListView(APIView):
    permission_classes = (IsAuthenticated,)
    
    '''
       Used for searching by properties or listing all friend requests received available.
    '''
    
    def get(self, request):
        '''
            Used to get all friends requests receieved of a user
        '''
        # get the offset and limit query parameters
        form = ReceivedGetListForm(request.QUERY_PARAMS)
        
        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()
        
class ReceivedSingleView(APIView):
    permission_classes = (IsAuthenticated,)
    
    '''
       Accepting, denying, and viewing requests received.
    '''     
    
    def put(self, request, user_id):
        '''
            Accept friend request.
        '''
        data = { key : request.DATA[key] for key in request.DATA }
        data['user_id'] = user_id
        form = ReceivedPutForm(data)

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()
        
    def delete(self, request, user_id):
        '''
            Deny friend request.
        '''
        form = ReceivedDeleteForm({ 'user_id' : user_id })

        if form.is_valid():
            return Response(form.submit(request))
        else:
            raise BadRequestException()
