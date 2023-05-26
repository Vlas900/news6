from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View



class LoginRequiredViewMixin(LoginRequiredMixin):
    login_url = '/login/'  # Замените на ваш URL для страницы входа в систему
    redirect_field_name = 'next'  # Параметр для указания перенаправления после успешного входа


class MyView(PermissionRequiredMixin, View):
    permission_required = ('simpleapp.add_post', 'simpleapp.change_post')
