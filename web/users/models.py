# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

GENDER_CHOICES = (
    ('U', 'Unknown'),
    ('F', 'Female'),
    ('M', 'Male'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Re-implementation of Django user model without pesky 'username' field.

    Copied from django.contrib.auth.models
    """
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    email = models.EmailField(_('email address'), max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=50, blank=True)
    last_name = models.CharField(_('last name'), max_length=50, blank=True, default='')
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Un-select this instead of deleting accounts.'))
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES, blank=True,
                              default=GENDER_CHOICES[0][0])
    born_on = models.DateTimeField(null=True, blank=True,
                                   help_text=_('Timestamp of the Spotter Birthday.'))

    date_joined = models.DateTimeField(_('date joined'), default=timezone.now,
                                       help_text=_('Designates when the user joined the SpotsTrek.'))

    lives_at = models.OneToOneField('Address', on_delete=models.SET_NULL, blank=True, null=True)
    phone_number = models.CharField(max_length=10, default='', blank=True, null=True)
    marked_inactive_because = models.CharField(max_length=255, default='', blank=True, null=True)
    marked_inactive_at = models.DateTimeField(null=True, blank=True, default=None)

    # -----------------------# Start Django-required Methods #-----------------------#
    def __unicode__(self):
        return self.email

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class Address(models.Model):
    street1 = models.CharField(_('street 1'), max_length=255, blank=True, default='')
    street2 = models.CharField(_('street 2'), max_length=255, blank=True, default='')
    city = models.CharField(_('city'), max_length=255, blank=True, default='')
    state = models.CharField(max_length=20, default='', blank=True)
    zip_code = models.CharField(_('zip code'), max_length=10, blank=True, default='')

    def __str__(self):
        return u'%s, %s, %s, %s %s' % (self.street1, self.street2, self.city, self.state, self.zip_code)
