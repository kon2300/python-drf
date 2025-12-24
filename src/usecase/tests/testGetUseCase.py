from typing import TypedDict


class TestGetResponse(TypedDict):
    message: str

class TestGetUseCase():
    def execute() -> TestGetResponse:
        resText: str = "Hello, World!"
        return {"message": resText}