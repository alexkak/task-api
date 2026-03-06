class AppException(Exception):
    def __init__(self, status_code: int, code: str, message: str):
        self.status_code = status_code
        self.code = code
        self.message = message

class NotFoundException(AppException):
    def __init__(self, message: str = "Resource not found"):
        super().__init__(status_code=404, code="NOT_FOUND", message=message)

class ValidationException(AppException):
    def __init__(self, message: str = "Validation error"):
        super().__init__(status_code=422, code="VALIDATION_ERROR", message=message)