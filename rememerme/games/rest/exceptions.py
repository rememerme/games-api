from rest_framework.exceptions import APIException

class BadRequestException(APIException):
    '''
        Bad Request Exception.
    '''
    status_code = 400
    detail = "A Bad Request was made for the API. Revise input parameters."
    
class RequestsListNotFoundException(APIException):
    '''
        The requested friends list was not found.
    '''
    status_code = 404
    detail = "The user is a total loser and has no friends. Please be more social."

class AlreadyFriendsException(APIException):
    '''
        The user requested to be a friend is already a friend.
    '''
    status_code = 400
    detail = "The user is already your friend. Why you friending him again?"

class RequestAlreadySentException(APIException):
    '''
        The user has already sent a friend request to a specific user.
    '''
    status_code = 400
    detail = "Dude. You already sent a request. Call'm if you want to be friends so bad. Jeez."

class UserNotFoundException(APIException):
    '''
        The user is not part of the system.
    '''
    status_code = 404
    detail = "You are not apparently part of the system."

class NotImplementedException(APIException):
    '''
        The API method was not implemented yet.
    '''
    status_code = 404
    detail = "This API method has not been implemented"

class FriendsListNotFoundException(APIException):
    '''
        The requested user was not found.
    '''
    status_code = 404
    detail = "The user is a total loser and has no friends. Please be more social."  
    
class FriendNotFoundException(APIException):
    '''
        The requested friend was not found.
    '''
    status_code = 404
    detail = "The user should not try to talk to people he doesn't know."
    
class RequestNotFoundException(APIException):
    '''
        The request does not exist between the two users.
    '''
    status_code = 404
    detail = "They never tried to be your friend. So why do you care so much?"
    
