from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from django.middleware import csrf
from django.contrib.auth import authenticate
from django.conf import settings
from .authenticate import CustomAuthentication
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class Register(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Login(APIView):
    def post(self, request):
        data = request.data
        response = Response()
        username = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=username, password=password)

        if user is None:
            raise AuthenticationFailed("Invalid Credentials!")

        token = get_tokens_for_user(user)
        response.set_cookie(
            key=settings.SIMPLE_JWT['AUTH_COOKIE'],
            value=token["access"],
            expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        response.set_cookie(
            key=settings.SIMPLE_JWT['REFRESH_COOKIE'],
            value=token["refresh"],
            expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
            secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
            httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
            samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
        )

        csrf.get_token(request)
        serializer = UserSerializer(user)
        response.data = {"Success": "Login successfully", "data": serializer.data}
        return response


class UserView(APIView):

    def post(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class DeleteUserView(APIView):

    def delete(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        user.delete()
        return Response({'message': 'Successfully deleted user: ' + serializer.data['email']})


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        response.delete_cookie("csrftoken")
        response.data = {
            'message': 'Success Logout'
        }
        return response


class RefreshTokenView(APIView):
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        data = {"refresh": request.COOKIES.get(
                settings.SIMPLE_JWT['REFRESH_COOKIE'])}
        print(data)
        serializer = TokenRefreshSerializer(data=data)
        response = Response()

        try:
            serializer.is_valid(raise_exception=True)
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=serializer.validated_data['access'],
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE']
            )
            response.data = {"Success": "Updated token successfully"}
        except TokenError as e:
            raise InvalidToken(e.args[0])

        return response