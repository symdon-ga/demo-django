import json
import base64

import urllib.parse
import requests

from django.conf import settings
from django.http import HttpResponse
from django.views.generic import View

from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages

class LoginView(View):
    def post(self, request):
        if request.user.is_authenticated:
            return redirect("/")
        return redirect(urllib.parse.urljoin(
            settings.SYMDON_AUTH_AUTH_URL,
            "?" + "&".join(f"{key}={urllib.parse.quote(val)}" for key, val in [
                ("client_id", settings.SYMDON_AUTH_CLIENT_ID),
                ("redirect_uri", settings.SYMDON_AUTH_REDIRECT_URI),
                ("response_mode", "query"),
                ("response_type", "code"),
                ("scope", "openid"),
                ("state", "f4850b2b-41ed-4869-83b1-a092f8eed6bf"),
                ("nonce", "9fa3ef48-a49a-4cde-8b3a-564a418a3002"),
            ])))

            
class LogoutView(View):
    def post(self, request):
        if request.user.is_authenticated:
            resp = requests.post(
                f"https://auth.symdon.ga/auth/realms/{settings.SYMDON_AUTH_REALM}/protocol/openid-connect/logout",
                headers={
                    "Authorization": f"Bearer {request.user.userlink.access_token}",
                },
                data={
                    "client_id": settings.SYMDON_AUTH_CLIENT_ID,
                    "refresh_token": request.user.userlink.refresh_token,
                })
            if resp.ok:
                request.user.userlink.clear_tokens().save()
                logout(request)
                messages.add_message(request, messages.INFO, "ログアウトしました")
            else:
                logger.error("Cannot logout: response body=%s", res.content)
                messages.add_message(request, messages.INFO, "ログアウトができませんでした。時間を置いてから再度ログアウトしてください。")
        return render(request, "logout.html")


class LoginCallbackView(View):
    def get(self, request, *args, **kwargs):
        from apps.symdon_auth.models import UserLink
        from django.contrib.auth import get_user_model
        from django.contrib.auth import login

        resp = requests.post(
            f"https://auth.symdon.ga/auth/realms/{settings.SYMDON_AUTH_REALM}/protocol/openid-connect/token",
            data={
                "client_id": settings.SYMDON_AUTH_CLIENT_ID,
                "code": request.GET["code"],
                "grant_type": "authorization_code",
                "redirect_uri": settings.SYMDON_AUTH_REDIRECT_URI,
            })

        resp_data = resp.json()
        header, payload, signature = resp_data["id_token"].split(".")
        claim_alist = json.loads(base64.b64decode(urllib.parse.unquote(payload)))
        userlink = UserLink.objects.filter(
            kind="symdon",
            realm=settings.SYMDON_AUTH_REALM,
            sub=claim_alist["sub"],
        ).first()

        if not userlink:
            user = get_user_model().objects.create()
            userlink = UserLink.objects.create(
                kind="symdon",
                realm=settings.SYMDON_AUTH_REALM,
                sub=claim_alist["sub"],
                user=user,
                access_token=resp_data["access_token"],
                refresh_token=resp_data["refresh_token"],
            )
        else:
            userlink.access_token = resp_data["access_token"]
            userlink.refresh_token = resp_data["refresh_token"]
            userlink.save()

            user = userlink.user
        login(request, user)
        messages.add_message(request, messages.INFO, "ログインしました")
        return redirect("/")


class TestView(View):
    def post(self, request, *args, **kwargs):
        import json
        from django.http import HttpResponse
        return HttpResponse(json.dumps({"text": "OK"}), content_type='application/json')
        
