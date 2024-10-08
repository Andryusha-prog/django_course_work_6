from django.contrib.auth.forms import UserCreationForm

from users.models import User


class UserRegisterView(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
