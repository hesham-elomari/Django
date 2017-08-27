from prompt_toolkit.validation import ValidationError

from myapp.models import User1
from rest_framework.serializers import ModelSerializer

class User1LoginSerializer(ModelSerializer):
    class Meta:
        model = User1
        fields = ( 'username', 'email', 'company_name','password')
        extra_kwargs={"password":{"write_only":True}}



class User1Serializer(ModelSerializer):
    class Meta:
        model = User1
        fields = ('id', 'username', 'email', 'company_name','job')








