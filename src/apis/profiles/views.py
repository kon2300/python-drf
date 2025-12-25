from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from src.apis.profiles.serializers.responseSerializers import UserProfileResponseSerializer
from src.usecase.profiles.getProfileUseCase import GetProfileUseCase
from src.usecase.profiles.dto.getProfileUseCaseDto import GetProfileUseCaseInput
from drf_spectacular.utils import extend_schema


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    get_profile_usecase = GetProfileUseCase()

    @extend_schema(
        responses=UserProfileResponseSerializer
    )
    def get(self, request):
        user = self.get_profile_usecase.execute(
            GetProfileUseCaseInput(user_id=request.user.id)
        )
        return Response(UserProfileResponseSerializer(user).data)
