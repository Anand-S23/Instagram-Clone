from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.conf import settings

# Create your models here.
USERNAME_REGEX = '^[a-zA-Z0-9]*$'


class MyUserManager(BaseUserManager):
	def create_user(self, username, email, name, password=None):
		if not email:
			raise ValueError('Users must enter an email address.')
		if not name: 
			raise ValueError('Users must enter full name.')

		user = self.model(username = username,
						  email = self.normalize_email(email),
						  name = name)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, username, email, name, password=None):
		user = self.create_user(username=username, 
								email=email, 
								name=name,
								password=password)
								
		user.is_admin = True
		user.is_staff = True
		user.save(using=self._db)
		return user


class MyUser(AbstractBaseUser):
	username = models.CharField(max_length=300,
								unique=True,
								validators = [RegexValidator(regex = USERNAME_REGEX,
															 message='Username must be alphanumeric or contain numbers.',
															 code='invalid_username')])

	email = models.EmailField(max_length=255, unique=True, verbose_name='Email Address')

	name = models.CharField(max_length=300, verbose_name="Full Name")

	bio = models.TextField(max_length=255,
						   verbose_name='Bio',
						   blank=True, 
						   null=True)
						   
	picture = models.ImageField(verbose_name='Profile Picture',
								blank=True, 
								upload_to='profile_pic',
								default='/profile_pic/default.jpg')
	
	followers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_follower')
	following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='user_following')

	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'name']

	def __str__(self):
		return str(self.username)
	
	def get_absolute_url(self):
		return reverse('accounts:detail', kwargs={'username': self.username})

	def get_short_name(self):
		return str(self.username)

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perms(self, app_label):
		return True

