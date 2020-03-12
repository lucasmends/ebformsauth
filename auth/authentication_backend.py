from django.contrib.auth.backends import ModelBackend
from .models import User
from .service import get_user
import logging


class AuthenticationBackend(ModelBackend):

    logger = logging.getLogger(__name__)

    def authenticate(self, request, username=None, password=None, **kwargs):
        if get_user(username, password) is None:
            return None

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User(username=username)
            user.save()
            logger.debug("Criado o usuário {}".format(username))
        
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            logger.debug("Usuario informado não existe")
            return None