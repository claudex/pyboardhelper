import uuid
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from authlib.integrations.django_client import OAuth

from .models import OAuth2Token


def index(request):
    context = {}
    return render(request, 'boardauth/index.html', context)

def login(request):
    oauth = OAuth(update_token=_update_token)
    oauth.register(name='dlfp')
    dlfp = oauth.create_client('dlfp')
    redirect_uri = 'https://localhost:8443/boardauth/oauth'  # reverse('oauth')
    return dlfp.authorize_redirect(request, redirect_uri)

def oauth_view(request):
    oauth = OAuth(update_token=_update_token)
    oauth.register(name='dlfp')
    dlfp = oauth.create_client('dlfp')
    token = dlfp.authorize_access_token(request)
    resp = dlfp.get('me', token=token)
    profile = resp.json()
    login = profile['login']

    dbToken = OAuth2Token.objects.filter(username=login).first()
    if not dbToken:
        dbToken = OAuth2Token(
            name='dlfp',
            uuid=uuid.uuid4(),
            username=login,
        )

    dbToken.token_type = token['token_type']
    dbToken.access_token = token['access_token']
    dbToken.refresh_token = token['refresh_token']
    dbToken.expires_at = token['expires_at']

    dbToken.save()

    context = {'uuid': dbToken.uuid}
    return render(request, 'boardauth/oauth.html', context)


@csrf_exempt
def post_dlfp(request):
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(request.POST)

    user_uuid = request.COOKIES['uuid']
    oauth = OAuth(update_token=_update_token)
    oauth.register(name='dlfp')
    dlfp = oauth.create_client('dlfp')
    token = OAuth2Token.objects.filter(uuid=user_uuid).first()
    message = request.POST['board[message]'] if 'board[message]' in request.POST else request.POST['message']
    resp = dlfp.post('board', json={'message': message}, token=token.to_token())

    return HttpResponse(resp)


def _update_token(name, token, refresh_token=None, access_token=None):
    if refresh_token:
        item = OAuth2Token.objects.filter(name=name, refresh_token=refresh_token).first()
    elif access_token:
        item = OAuth2Token.objects.filter(name=name, access_token=access_token).first()
    else:
        return

    # update old token
    item.access_token = token['access_token']
    item.refresh_token = token.get('refresh_token')
    item.expires_at = token['expires_at']
    item.save()

