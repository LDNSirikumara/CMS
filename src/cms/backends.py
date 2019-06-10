# from django.contrib.auth.models import User
# from django.core.exceptions import MultipleObjectsReturned

# class EmailBackend(object):
#     def authenticate(self, username=None, password=None,**kwargs):
#         try:
#             user = User.objects.get(email=username)
#         except User.MultipleObjectsReturned:
#             user = User.objects.filter(email=username).order_by('id').first()
#         except User.DoesNotExist:
#             return None

#         if getattr(user, 'is_active')and user.check_password(password):
#             return user
#         return None
        
#     def get_user(self, user_id):
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

# class EmailBackend(ModelBackend):
#     def authenticate(self, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         try:
#             user = UserModel.objects.get(email=username)
#         except UserModel.DoesNotExist:
#             return None
#         else:
#             if user.check_password(password):
#                 return user
#         return None




# from django.contrib.auth import get_user_model  # gets the user_model django  default or your own custom
# from django.contrib.auth.backends import ModelBackend
# from django.db.models import Q


# # Class to permit the athentication using email or username
# class CustomBackend(ModelBackend):  # requires to define two functions authenticate and get_user

#     def authenticate(self, username=None, password=None, **kwargs):
#         UserModel = get_user_model()

#         try:
#             # below line gives query set,you can change the queryset as per your requirement
#             user = UserModel.objects.filter(
#                 Q(username__iexact=username) |
#                 Q(email__iexact=username)
#             ).distinct()

#         except UserModel.DoesNotExist:
#             return None

#         if user.exists():
#             ''' get the user object from the underlying query set,
#             there will only be one object since username and email
#             should be unique fields in your models.'''
#             user_obj = user.first()
#             if user_obj.check_password(password):
#                 return user_obj
#             return None
#         else:
#             return None

#     def get_user(self, user_id):
#         UserModel = get_user_model()
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
#             return None

from django.contrib.auth import backends, get_user_model
from django.db.models import Q
UserModel = get_user_model()


class ModelBackend(backends.ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        try:
            # user = UserModel._default_manager.get_by_natural_key(username)
            # You can customise what the given username is checked against, here I compare to both username and email fields of the User model
            user = UserModel.objects.get(Q(username__iexact=username) | Q(email__iexact=username))
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        return super().authenticate(request, username, password, **kwargs)