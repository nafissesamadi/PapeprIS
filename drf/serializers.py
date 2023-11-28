from rest_framework import serializers
from paper.models import Paper,Author

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paper
        fields=['title','field_research','authors','keywords','published_in','citation']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['username', 'first_name', 'Auth_paper']