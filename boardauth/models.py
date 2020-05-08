""" DB models for auth """
from django.db import models


class DlfpAuth(models.Model):
    """ Store the mapping betweend the id sent and the DLFP oauth reference """
    oauth_referecne = models.CharField(max_length=256)
    cookie_id = models.CharField(max_length=64)


class OAuth2Token(models.Model):
    name = models.CharField(max_length=40)
    token_type = models.CharField(max_length=40)
    access_token = models.CharField(max_length=200)
    refresh_token = models.CharField(max_length=200)
    expires_at = models.PositiveIntegerField()
    uuid = models.CharField(max_length=64)
    username = models.CharField(max_length=200)

    def to_token(self):
        return dict(
            access_token=self.access_token,
            token_type=self.token_type,
            refresh_token=self.refresh_token,
            expires_at=self.expires_at,
        )


class EuroLogin(models.Model):
    """ Credentials for euromussels """
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    cookie = models.CharField(max_length=64)
    oauth_token = models.OneToOneField(OAuth2Token, on_delete=models.CASCADE)
