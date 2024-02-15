from django.shortcuts import render
from .serializer import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_auth.registration.views import RegisterView
from  .models import CustomUser


class UserList(generics.ListCreateAPIView, mixins.ListModelMixin,
                mixins.CreateModelMixin, mixins.UpdateModelMixin, 
                mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        if id :
            return self.retrieve(request)
        else:
            return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
    def put(self, request, id=None):
        return self.update(request, id)
    
    def delete(self, request, id=None):
        return self.destroy(request, id)