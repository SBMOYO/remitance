import pytest
from django.test import Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status


@pytest.mark.django_db
def test_user_list_get():
    client = Client()
    response = client.get(reverse('user-list'))
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_list_post():
    client = Client()
    data = {
        'email': 'user@example.com',
        'password': 'password',
        # Add other fields here
    }
    response = client.post(reverse('user-list'), data)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_user_list_put():
    User = get_user_model()
    user = User.objects.create_user(email='user@example.com', password='password')
    client = Client()
    data = {
        'email': 'newuser@example.com',
        # Add other fields here
    }
    response = client.put(reverse('user-detail', kwargs={'id': user.id}), data)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_user_list_delete():
    User = get_user_model()
    user = User.objects.create_user(email='user@example.com', password='password')
    client = Client()
    response = client.delete(reverse('user-detail', kwargs={'id': user.id}))
    assert response.status_code == status.HTTP_204_NO_CONTENT