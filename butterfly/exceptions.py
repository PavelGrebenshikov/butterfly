class HttpErrorException(Exception):
    def __init__(self, status_code: int):
        self.status_code = status_code
