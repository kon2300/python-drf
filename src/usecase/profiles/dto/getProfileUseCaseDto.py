from dataclasses import dataclass


@dataclass(frozen=True)
class GetProfileUseCaseInput:
    user_id: int
