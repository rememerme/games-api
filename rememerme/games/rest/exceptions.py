from rest_framework.exceptions import APIException

class BadRequestException(APIException):
    '''
        Bad Request Exception.
    '''
    status_code = 400
    detail = "A Bad Request was made for the API. Revise input parameters."
    
class InvalidWinningScore(APIException):
    '''
        The winning score was not greater than 0.
    '''
    status_code = 400
    detail = "You can't setup a game if the score doesn't make sense."

class IllegalStatusCode(APIException):
    '''
        The code for the game member status is out of range.
    '''
    status_code = 40
    detail = "The code for the game member status is out of range."

class GameNotFound(APIException):
    '''
        The game requested was not found.
    '''
    status_code = 404
    detail = "Don't ask about that game because we have no idea what you are talking about."

class GameMemberNotFound(APIException):
    '''
        The game member was not found
    '''
    status_code = 404
    detail = "You are not apparently part of this game or something."

class GameMemberAlreadyExists(APIException):
    '''
        Game Memberalready exists.
    '''
    status_code = 404
    detail = "You've already invited him to the game! Be more needy!"

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
    
