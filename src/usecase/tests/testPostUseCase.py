from typing import TypedDict


class TestPostResponse(TypedDict):
    message: str

class TestPostUseCase():
    def execute(self, data) -> TestPostResponse:
        resText: str = data.get("text", "Hello, World!")
        return {"message": resText}