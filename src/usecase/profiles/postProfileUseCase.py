from src.usecase.profiles.dto.postProfileUseCaseDto import PostTestUseCaseOutput
from src.usecase.profiles.dto.postProfileUseCaseDto import PostTestUseCaseInput


class TestPostUseCase:
    def execute(self, data: PostTestUseCaseInput) -> PostTestUseCaseOutput:
        resText: str = data.token
        return PostTestUseCaseOutput(message=resText)
