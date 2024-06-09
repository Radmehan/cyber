from django.http import HttpResponse

def admin_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You don't have permission to access this page.", status=403)  # 403 Forbidden
    return _wrapped_view

