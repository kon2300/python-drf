from dataclasses import dataclass


@dataclass
class PostProfileUseCaseOutput:
    message: str

@dataclass
class PostProfileUseCaseInput:
    token: str