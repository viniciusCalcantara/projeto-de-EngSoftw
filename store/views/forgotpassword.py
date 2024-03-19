from django.shortcuts import render
from django.core.mail import send_mail
from django.views import View
from django.conf import settings
from store.models.customer import Customer

class ForgotPassword(View):
    def get(self, request):
        return render(request, 'forgotpassword.html')

    def post(self, request):
        email = request.POST.get('email')
        customer = Customer.get_customer_by_email(email)
        if customer:
            # Lógica para gerar e enviar o email de recuperação de senha
            # Aqui você pode gerar um token de recuperação de senha e enviar um email com um link contendo esse token
            token = 'abcd1234'  # Exemplo de token gerado, você precisa implementar a lógica real aqui
            reset_link = f"http://{request.get_host()}/reset_password?token={token}"  # URL para a página de redefinição de senha com o token
            send_mail(
                'Password Reset Request',
                f'Please click the following link to reset your password: {reset_link}',
                settings.EMAIL_HOST_USER,  # Deve ser configurado nas suas configurações
                [email],
                fail_silently=False,
            )
            # Renderiza uma página informando ao usuário que um email de recuperação de senha foi enviado
            return render(request, 'password_reset_email_sent.html')
        else:
            # Se o email não estiver associado a nenhum usuário, renderiza novamente a página de recuperação de senha com uma mensagem de erro
            return render(request, 'forgotpassword.html', {'error': 'Email not found.'})
