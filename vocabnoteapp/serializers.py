from rest_framework import  serializers
#from .models import User

from .models import  User
from .models import  Word
from .models import  Classification



class WordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('Word','Word')


class ClassSerializer(serializers.ModelSerializer):
    Word = WordsSerializer(many=True)

    class Meta:
        model = Classification
        fields = ('Classification','Word')

class Usererializer(serializers.ModelSerializer):
    Classification = ClassSerializer(many=True)

    class Meta:
        model = User
        fields = ('User_Auth_ID','User_Name','Email','Classification')