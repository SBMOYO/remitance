import pytest
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

@pytest.mark.django_db
def test_create_user():
    User = get_user_model()
    user = User.objects.create_user(
        email='user@example.com',
        password='password',
        first_name='First',
        last_name='Last',
        surname='Surname',
        identification_number='63R123456',
        phone_number='1234567890',
        residential_address='123 Street'
    )
    assert user.email == 'user@example.com'
    assert user.first_name == 'First'
    assert user.last_name == 'Last'
    assert user.surname == 'Surname'
    assert user.identification_number == '63R123456'
    assert user.phone_number == '1234567890'
    assert user.residential_address == '123 Street'
    assert user.is_staff is False
    assert user.is_admin is False
    assert user.is_superuser is False


@pytest.mark.django_db
def test_user_string_representation():
    User = get_user_model()
    user = User.objects.create_user(
        email='user@example.com',
        password='password',
        first_name='First',
        last_name='Last',
        surname='Surname',
    )
    assert str(user) == 'First Surname user@example.com'


@pytest.mark.django_db
def test_user_has_perm():
    User = get_user_model()
    user = User.objects.create_user(
        email='user@example.com',
        password='password',
        is_admin=True
    )
    assert user.has_perm(None) is True


@pytest.mark.django_db
def test_user_has_module_perms():
    User = get_user_model()
    user = User.objects.create_user(
        email='user@example.com',
        password='password',
    )
    assert user.has_module_perms(None) is True