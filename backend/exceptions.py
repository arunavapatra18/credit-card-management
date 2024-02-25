from fastapi import HTTPException, status

class CustomException:
    class EmailAlreadyTakenException(HTTPException):
        def __init__(self, detail="Email already taken!"):
            super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
        
    class DatabaseOperationException(HTTPException):
        def __init__(self, detail):
            super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)
            
    class UserNotfoundException(HTTPException):
        def __init__(self, detail="User not found!"):
            super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)
            
    class IncorrectPasswordOrEmailException(HTTPException):
        def __init__(self, detail="Incorrect password or email!"):
            super().__init__(status_code=status.HTTP_401_UNAUTHORIZED, detail=detail)

    class CardAlreadyAddedException(HTTPException):
        def __init__(self, detail="Card already added!"):
            super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)