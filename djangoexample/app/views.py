from django.http import HttpResponse
from django.views.generic import View


class PingPongView(View):
    def get(self, request, *args, **kwds):
        return HttpResponse('PONG (GET)')

    def post(self, request, *args, **kwds):
        return HttpResponse('PONG (POST)')
