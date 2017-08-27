from rest_framework.response import Response
from rest_framework.generics import ListAPIView,RetrieveAPIView,CreateAPIView
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from myapp.models import User1
from .serializers import User1Serializer,User1LoginSerializer

class User1View(ListAPIView):
    queryset = User1.objects.all()
    serializer_class = User1Serializer


class User1DetailView(RetrieveAPIView):
    queryset = User1.objects.all()
    serializer_class = User1Serializer
    lookup_field = 'job'

class User1CreateView(CreateAPIView):
    queryset = User1.objects.all()
    serializer_class = User1Serializer

class User1LoginView(APIView):

    serializer_class = User1LoginSerializer
    def post(self,request,*args,**kwargs):
        data = request.data
        serializer = User1LoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data ,status=HTTP_200_OK)
        return Response(serializer.errors , status = HTTP_400_BAD_REQUEST)

