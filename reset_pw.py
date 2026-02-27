import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'dacol' # SEU USUÁRIO AQUI
new_password = '123' # SUA SENHA NOVA AQUI

try:
    u = User.objects.get(username=username)
    u.set_password(new_password)
    u.save()
    print(f"Sucesso: Senha de {username} atualizada!")
except User.DoesNotExist:
    # Se o usuário não existir, ele cria um novo
    User.objects.create_superuser(username, 'admin@email.com', new_password)
    print(f"Sucesso: Superusuário {username} criado!")