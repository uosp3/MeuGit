Iniciar o projeto Django

```
python -m venv venv
. venv/Scripts/activate
pip install django
django-admin startproject project .
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

git push origin master   <!-- enviar os arquivos -->