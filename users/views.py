from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import CustomUserCreationForm
from django.core.mail import send_mail


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        # Сохраняем пользователя только если форма валидна
        user = form.save()
        # Отправляем приветственное письмо
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_welcome_mail(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = 'Poxxyuct812@yandex.ru'
        recipient_list = [user_email,]
        send_mail(subject, message, from_email, recipient_list)

