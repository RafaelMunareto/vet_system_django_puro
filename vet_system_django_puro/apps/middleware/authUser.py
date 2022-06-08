from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect


class ProcessRequestMiddleware(MiddlewareMixin):
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user = request.user
        
        if request.path == '/login/cadastro':
            pass        
        elif request.path == '/login':
            pass
        else:
            if user.is_authenticated:
                pass
            else:
                return redirect("login")
        