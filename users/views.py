from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from config.settings import EMAIL_HOST_USER

from .forms import CustomUserCreationForm


class RegisterView(CreateView):
    template_name = "users/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("catalog:home")

    def form_valid(self, form):
        # Сохраняем пользователя только если форма валидна
        user = form.save()
        login(self.request, user)
        # Отправляем приветственное письмо
        self.send_welcome_mail(user.email)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def send_welcome_mail(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = EMAIL_HOST_USER
        recipient_list = [
            user_email,
        ]
        send_mail(subject, message, from_email, recipient_list)
