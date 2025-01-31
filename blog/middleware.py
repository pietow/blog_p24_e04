from django.contrib.auth.models import User
from django.urls import reverse , resolve
from django.http import HttpResponseRedirect

class SpecialUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user_id = request.session.get('_auth_user_id')
        if user_id:
            user = User.objects.get(pk=user_id)
            return HttpResponse(f"You are {user}!")

        response = self.get_response(request)

        response.write('You not logged in!')

        return response

class ProtectSpecificRoutesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        protected_url_names = [
            'post_new',
            'post_edit',
            'post_delete',
        ]
        current_url_target_name = resolve(request.path_info).url_name

        if current_url_target_name in protected_url_names\
                        and not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))

        response = self.get_response(request)

        return response

