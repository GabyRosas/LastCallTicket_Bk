from rest_framework import generics, permissions, views, status
from django.contrib.auth.models import User
from .serializer import RegisterSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class LogoutView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({"message": "Token deleted"}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({"message": "Token not found"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_user_id(request, username):
    try:
        user = User.objects.get(username=username)
        return Response({'id': user.id})
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=404)