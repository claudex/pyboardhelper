#!/usr/bin/env python
""" Script to run to update euromussels cookie """
import os
import requests

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pyboardhelper.settings")
django.setup()


from boardauth.models import EuroLogin


def main():
    """ Connect to euromussels and request a new cookie """
    for eurologin in EuroLogin.objects.all():
        session = requests.session()
        req = session.post(
            'https://faab.euromussels.eu/loginA.php',
            data={'login': eurologin.username, 'password': eurologin.password,
            'action': 'Login'})
        cookie = session.cookies['faab_id']
        eurologin.cookie = cookie
        eurologin.save()


if __name__ == '__main__':
    main()
