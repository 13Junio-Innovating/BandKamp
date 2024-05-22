from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from .permissions import IsAccountOwner
from .models import User
from .serializers import UserSerializer

class UserView(CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "pk"
