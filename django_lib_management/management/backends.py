from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import *

#To handle Tthe log in functionality as per requirement
class EmailBackend(ModelBackend):
	def authenticate(self, request, username=None, password=None, **kwargs):
		try:
			user = CustomUser.objects.get(Q(email__iexact=username))
		except CustomUser.DoesNotExist:
			CustomUser().set_password(password)
			return
		except CustomUser.MultipleObjectsReturned:
			user = CustomUser.objects.filter(Q(email__iexact=username))

		if user.check_password(password) and self.user_can_authenticate(user):
			return user
"""Here requirement is to log only with email _id as username and password, from model we check for the email as username"""
