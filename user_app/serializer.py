from rest_framework import serializers
from django.contrib.auth.models import User


# Serializamos la data que trae ese objeto, en este caso el objeto User
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        # Le decimos cuáles son los campos de mi modelo que quiero que me estructure. Serialización de la data. Aquí
        # le decimos que queremos que serialice todos los campos
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
