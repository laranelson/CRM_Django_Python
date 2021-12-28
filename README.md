<<<<<<< HEAD
# crm

Passo para criar novo APP

1 - Primeir passo
>$ python manage.py startapp name_app

2 - Registrar no script settings.py em INSTALLED_APPS

3 - Criar dentro do novo app o script urls.py depois registrar dentro do script urls.py principal

3 - Criar as tabelas em models.py

4 - Criar o script forms.py

5 - Criar o script views.py
   
    # 1 - Digitar no terminal >>> python manage.py makemigrations nomedoapp
    # 2 - Depois digitar o comando >>> python manage.py migrate
    # 3 - Agora é preciso registrar a tabela no arquivo admin.py from .models import nomedoapp
=======
Essa aplicação encontra-se hospedada através do Keroku acesse em: https://crrm.herokuapp.com
Utilize o usuário: admin
e a senha: admin
>>>>>>> a911b73fefa12f6b50916d87774dc143c37f3ae8
