from src.usecase.profiles.dto.getProfileUseCaseDto import GetProfileUseCaseInput
from django.contrib.auth import get_user_model

User = get_user_model()


class GetProfileUseCase:
    def execute(self, input_data: GetProfileUseCaseInput) -> User:
        user = User.objects.select_related("profile").get(id=input_data.user_id)

        return user
