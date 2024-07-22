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