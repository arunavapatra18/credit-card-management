from fastapi import HTTPException, status

class EmailAlreadyTakenException(HTTPException):
    def __init__(self, detail="Email already taken!"):
        super().__init__(status_code=status.HTTP_409_CONFLICT, detail=detail)
    
class DatabaseOperationException(HTTPException):
    def __init__(self, detail):
        super().__init__(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=detail)