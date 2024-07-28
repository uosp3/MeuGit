# type: ignore
# flake8: noqa

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


Para habilitar o autocompletar de tags HTML em arquivos de templates Django no VS Code, você pode seguir algumas etapas para configurar corretamente o editor. O VS Code não reconhece automaticamente arquivos de template Django como arquivos HTML, então precisamos ajustar algumas configurações para garantir que o autocompletar funcione como esperado.

### Passos para Configurar o VS Code

1. **Extensão para Django**:
   - Instale uma extensão que suporte Django. A extensão "Django" ou "Django Template" pode ajudar a adicionar suporte adicional para a sintaxe do Django no VS Code.

2. **Configurar o Idioma do Arquivo**:
   - Certifique-se de que o VS Code está tratando seus arquivos de template Django como arquivos HTML. Você pode fazer isso manualmente no editor:
     - Abra um arquivo de template Django.
     - Clique no ícone de seleção de linguagem no canto inferior direito do VS Code (onde aparece o tipo de arquivo, por exemplo, "Plain Text").
     - Selecione "Configure File Association for ‘.html’" ou "Change Language Mode".
     - Escolha "HTML" na lista de opções.

3. **Configurações do Workspace**:
   - Adicione configurações específicas ao seu workspace para reconhecer arquivos de template Django como HTML:
     - Abra as configurações do VS Code (Ctrl + ,).
     - No campo de busca, digite "files.associations".
     - Clique em "Edit in settings.json" para adicionar a seguinte configuração:
       ```json
       "files.associations": {
           "*.html": "html",
           "*.htm": "html",
           "*.djhtml": "html",
           "*.jinja": "html"
       }
       ```
     - Substitua ou adicione quaisquer extensões específicas que você usa para templates Django.

4. **Emmet no VS Code**:
   - Emmet é uma ferramenta poderosa para autocompletar e pode ser configurada para funcionar em arquivos HTML:
     - Abra as configurações do usuário ou do workspace no VS Code.
     - Adicione ou verifique se a configuração do Emmet está habilitada:
       ```json
       "emmet.includeLanguages": {
           "django-html": "html"
       }
       ```
     - Isso garante que o Emmet trate arquivos de template Django como HTML para autocompletar.

5. **Recarregar o VS Code**:
   - Após fazer essas alterações, recarregue o VS Code para que as configurações sejam aplicadas.

Essas etapas devem ajudar a ativar o autocompletar para tags HTML em arquivos de templates Django no VS Code. Se você continuar enfrentando problemas, verifique se as extensões estão atualizadas e se não há conflitos com outras configurações.