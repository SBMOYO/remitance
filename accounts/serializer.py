from .models import CustomUser
from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        field = ['email', 'password', 'first_name', 'last_name', 'surname', 'date_of_birth', 'identification_number', 'phone_number', 'residential_address', 'is_staff', 'is_admin', 'is_superuser']



class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    surname = serializers.CharField(required=True)
    date_of_birth = serializers.DateField(required=True)
    identification_number = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    residential_address = serializers.CharField(required=True)

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return {
            "first_name": self.validated_data.get('first_name', ''),
            "last_name": self.validated_data.get('last_name', ''),
            "surname": self.validated_data.get('surname', ''),
            "email": self.validated_data.get('email', ''),
            "password1": self.validated_data.get('password1', ''),
            "password2": self.validated_data.get('password2', ''),
            "date_of_birth": self.validated_data.get('date_of_birth', ''),
            "identification_number": self.validated_data.get('identification_number', ''),
            "phone_number": self.validated_data.get('phone_number', ''),
            "residential_address": self.validated_data.get('residential_address', ''),
        }