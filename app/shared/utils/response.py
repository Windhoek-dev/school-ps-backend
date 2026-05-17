from fastapi import status


class Response:
    def __init__(
        self,
        data: object = None,
        message: str = "Success",
        status_code: int = status.HTTP_200_OK,
        details: dict | None = None,
    ):
        self.data = data
        self.status_code = status_code
        self.message = message
        self.details = details

    def to_dict(self) -> dict:
        return {
            "statusCode": self.status_code,
            "data": self.data,
            "message": self.message,
            "details": self.details,
        }
