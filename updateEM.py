#!/usr/bin/env python
""" Script to run to update euromussels cookie """
import os
import time
import requests

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyboardhelper.settings")
django.setup()


from boardauth.models import EuroLogin

def updateCookie(eurologin):
    session = requests.session()
    req = session.post(
        'https://faab.euromussels.eu/loginA.php',
        data={'login': eurologin.username, 'password': eurologin.password,
        'action': 'Login'})
    cookie = session.cookies['faab_id']
    eurologin.cookie = cookie
    eurologin.save()

def main():
    """ Connect to euromussels and request a new cookie """
    for eurologin in EuroLogin.objects.all():
        try:
            updateCookie(eurologin)
        except Exception as e:
            print(e)
            time.sleep(5)
            updateCookie(eurologin)


if __name__ == '__main__':
    main()
