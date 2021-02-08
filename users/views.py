from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import SignUpForm
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token


class SignUpView(View):
    form_class = SignUpForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.warning(request, 'Faça o logout primeiro')
            return redirect('projetos')

        form = self.form_class()
        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():

            user = form.save(commit=False)
            user.is_active = False
            user.save()

            current_site = get_current_site(request)
            subject = 'Ative sua conta no ITeamManager'
            protocol = 'https' if request.is_secure() else 'http'

            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'protocol': protocol,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message, html_message=message)

            messages.success(request, 'Um email de ativação foi enviado. Verifique na caixa de spam ou exluídos\n'
                                      'Ps: Caso você faça o login sem ativar a conta, irá constar como se a senha ou'
                                      'usuário estão incorretos')

            return redirect('login')

        return render(request, 'registration/signup.html', {'form': form})


class ActivateAccount(View):
    @staticmethod
    def get(request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.profile.email_confirmed = True
            user.save()
            login(request, user)

            messages.success(request, 'Sua conta foi ativada!')
            return redirect('projetos')
        else:
            messages.warning(request, 'Este link de ativação é inválido')
            return redirect('signup')
