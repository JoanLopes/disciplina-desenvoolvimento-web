from django.contrib.auth import login, logout, authenticate
from django.views import View
from django.shortcuts import render, redirect
from login.forms import LoginForm
from django.conf import settings




class LoginView(View):
    form_class = LoginForm
    template_name = 'login.html'
    template_name2 = 'temp2.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()

        if request.user.is_authenticated:
            # Se o usuário já estiver autenticado, redirecione para a página inicial
             return render(request, self.template_name2, {'msg': 'teste'})
        else:
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)  # Autentica o usuário
            if user is not None and user.is_active:
                login(request, user)
                # Redirecione para onde quiser após o login
                return render(request, self.template_name, {'form': form})
            else:
                # Se o usuário não estiver ativo, exiba uma mensagem de erro ou redirecione para outra página
                # Aqui vamos redirecionar de volta para a página de login com uma mensagem de erro
                error_message = "Nome de usuário ou senha inválidos."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})
        return render(request, self.template_name, {'form': form})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        # Redirecione para onde quiser após o logout
        return redirect(settings.LOGIN_URL)