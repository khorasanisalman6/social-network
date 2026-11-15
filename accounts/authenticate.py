from accounts.models import User
from django.contrib.auth.backends import BaseBackend
class EmailAuthenticate(BaseBackend):
    def authenticate(self,request, username=None, password=None):
        if username is None and password is None:
            return None
        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password):
            return user
        return None



    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
