Iniciar o projeto Django

```
python -m venv venv
. venv/Scripts/activate
pip install django
django-admin startproject project .
python manage.py startapp contact  <!--- faz o mesmo que a linha acima mas para depois do projeto criado ->
<!-- depois de criado o app inclua-o em project(no arquivo settings.py) -->
```

Configurar o git

```
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .    <!-- adiciona todos os arquivos para o git (exceto ignore) fazer isto sempre que necessário, por exemplo em caso de alterações nos arquivos e em seguida fazer o commit -->
git commit -m 'Mensagem'
git log      <!-- para ver o que foi no commit -->
git remote add origin URL_DO_GIT
git push   <!-- enviar os arquivos -->



Alguns detalhes sobre o projeto
1   Dentro do meu app eu posso ter uma pasta chamada de templates, que vão ter templates que são relacionados com o epp em si.
2   Eu vou criar uma pasta aqui chamada de base_templates.
3   e eu vou criar uma outra pasta de base_static.
4   então dentro de base_templates eu vou criar um namespace global
5   vou criar dentro da pasta do global o arquivo base.html.
6   Fazer um glogal dentro de base_static e nele criar uma pasta css e nela um arquivo style.css

7   Fazer as configurações no settings.py (na pasta project):
    7.1     Nos TEMPLATES em 'DIRS':[
            BASE_DIR / 'base_templates'
            ],
    7.2     Nos STATIC colocar STATICFILES_DIRS = (
            BASE_DIR / 'base_static',
            )

8   Em 'contatc' criar a pasta 'templates' e nela criar uma pasta, também chamada 'contact', que é o nome do app.
    8.1     Criar em 'contact' um arquivo 'index.html' que será a home
            de 'contact'

9   Criar o arquivo 'urls.py' na pasta 'contact'
10  Criado o models.py fazer o registro em admin.py

=================================================
Migrando a base de dados do Django

python manage.py makemigrations  <!-- usar sempre que alterar o models.py -->
python manage.py migrate <!-- usar depois que executar a linha acima -->
Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword USERNAME <!-- esqueceu a senha? -->
=================================================

Documentação models:
https://docs.djangoproject.com/pt-br/4.2/topics/db/models/
https://docs.djangoproject.com/pt-br/4.2/ref/models/fields/#field-choices
